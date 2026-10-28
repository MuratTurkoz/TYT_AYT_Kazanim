"""Bir eşleştirme tablosundaki Sıra–kod bağını kaynakla denetler.

Kullanım:
    python araclar/sira_kod_dogrula.py <dosya.md | dosya.xlsx> [...]

Kaynak: kazanimlar/tum_kazanimlar.json (ALL BRANŞLAR KAZANIM.xlsx aktarımı).
Başlığı "Sıra" ile başlayan her tablo sütunu denetlenir: Sıra boş olmamalı
ve kaynakta bulunmalıdır. Aynı tabloda "Derinlik" ve "açıklama" içeren
sütunlar varsa Sıra'nın kaynak satırıyla karşılaştırılır. Kod sütunu varsa
uyuşmazlık yalnızca bilgi olarak yazılır; kod seçim ölçütü değildir.

Başlığında "A Soru no" ve "B Soru no" olan kitapçık tablosu varsa test başına
bire bir eşleşme denetlenir: A ve B numaraları yinelenmemeli, ana tablodaki
(başlığında "Kazanım açıklaması" olan) her soru kitapçık tablosunda bulunmalı
ve kitapçık tablosundaki Sıra ana tablodakiyle aynı olmalıdır.
"""

import html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

KAYNAK = Path(__file__).resolve().parent.parent / "kazanimlar" / "tum_kazanimlar.json"


def norm(s):
    s = html.unescape(str(s)).replace("<br>", " ")
    return re.sub(r"\s+", " ", s).strip()


def sira_oku(deger):
    """Sıra hücresini tamsayıya çevirir; 958754.0 gibi Excel değerlerini kabul eder."""
    if deger is None:
        return None
    if isinstance(deger, (int, float)) and float(deger).is_integer():
        return int(deger)
    s = str(deger).strip()
    return int(s) if s.isdigit() else s or None


def kaynak_yukle():
    veri = json.loads(KAYNAK.read_text(encoding="utf-8"))
    kayitlar = {r["serial"]: r for r in veri["records"]}
    kod_sira = defaultdict(list)
    for r in veri["records"]:
        kod_sira[norm(r["code"])].append(r["serial"])
    return kayitlar, kod_sira


def md_tablolari(yol):
    baslik = None
    for no, satir in enumerate(Path(yol).read_text(encoding="utf-8").splitlines(), 1):
        if not satir.startswith("|"):
            baslik = None
            continue
        hucreler = [h.strip() for h in satir.strip().strip("|").split("|")]
        if baslik is None:
            baslik = [h.lower() for h in hucreler]
        elif not set("".join(hucreler)) <= set("-: "):
            yield f"satır {no}", baslik, hucreler


def xlsx_tablolari(yol):
    import openpyxl

    kitap = openpyxl.load_workbook(yol, read_only=True, data_only=True)
    for sayfa in kitap:
        baslik = None
        for no, satir in enumerate(sayfa.iter_rows(values_only=True), 1):
            hucreler = list(satir)
            if baslik is None:
                if any(str(h or "").strip().lower().startswith("sıra") for h in hucreler):
                    baslik = [str(h or "").strip().lower() for h in hucreler]
                continue
            if any(h is not None for h in hucreler):
                yield f"{sayfa.title}!{no}", baslik, hucreler


def sutun(baslik, kosul):
    return next((i for i, h in enumerate(baslik) if kosul(h)), None)


def denetle(yol, kayitlar, kod_sira):
    satirlar = xlsx_tablolari(yol) if yol.lower().endswith(".xlsx") else md_tablolari(yol)
    adet, hatalar, bilgiler = 0, [], []
    for yer, baslik, hucreler in satirlar:
        si = sutun(baslik, lambda h: h.startswith("sıra"))
        if si is None:
            continue
        sira = sira_oku(hucreler[si]) if si < len(hucreler) else None
        if sira is None:
            # Kitapçık tablosunda Sıra'sı olmayan soru (ör. alternatif felsefe) olabilir.
            kitapcik = sutun(baslik, lambda h: h == "a soru no") is not None
            if not kitapcik and any(h not in (None, "") for h in hucreler):
                hatalar.append(f"{yer}: Sıra boş")
            continue
        adet += 1
        kayit = kayitlar.get(sira)
        if kayit is None:
            hatalar.append(f"{yer}: Sıra {sira} kaynakta yok")
            continue
        ki = sutun(baslik, lambda h: "kod" in h)
        if ki is not None and ki < len(hucreler) and hucreler[ki] not in (None, ""):
            verilen = norm(hucreler[ki])
            if verilen != norm(kayit["code"]):
                sahipler = [s for s in kod_sira.get(verilen, []) if s != sira]
                ek = f"; bu kod şu Sıra'lara ait: {sahipler}" if sahipler else ""
                bilgiler.append(f"{yer}: Sıra {sira} kodu {kayit['code']}, tabloda {verilen}{ek}")
        di = sutun(baslik, lambda h: h == "derinlik")
        if di is not None and di < len(hucreler) and hucreler[di] not in (None, ""):
            if str(sira_oku(hucreler[di])) != str(kayit["depth"]):
                hatalar.append(f"{yer}: Sıra {sira} derinliği {kayit['depth']}, tabloda {hucreler[di]}")
        ai = sutun(baslik, lambda h: "açıklama" in h)
        if ai is not None and ai < len(hucreler) and hucreler[ai] not in (None, ""):
            if norm(hucreler[ai]) != norm(kayit["description"]):
                hatalar.append(f"{yer}: Sıra {sira} açıklaması kaynakla aynı değil")
    return adet, hatalar, bilgiler


def kitapcik_denetle(yol):
    satirlar = xlsx_tablolari(yol) if yol.lower().endswith(".xlsx") else md_tablolari(yol)
    ana, kitapcik, hatalar = {}, [], []
    for yer, baslik, hucreler in satirlar:
        def al(kosul):
            i = sutun(baslik, kosul)
            return hucreler[i] if i is not None and i < len(hucreler) else None
        test = norm(al(lambda h: h == "test") or "").lower()
        sira = sira_oku(al(lambda h: h.startswith("sıra")))
        a = sira_oku(al(lambda h: h == "a soru no"))
        if a is not None or sutun(baslik, lambda h: h == "a soru no") is not None:
            b = sira_oku(al(lambda h: h == "b soru no"))
            durum = norm(al(lambda h: h == "durum") or "").lower()
            kitapcik.append((yer, test, a, b, sira, durum))
        elif sutun(baslik, lambda h: h == "kazanım açıklaması") is not None:
            no = sira_oku(al(lambda h: h == "soru no"))
            if no is not None:
                ana[(test, no)] = sira
    if not kitapcik:
        return 0, hatalar

    gorulen_a, gorulen_b = {}, {}
    for yer, test, a, b, sira, durum in kitapcik:
        if a is None:
            hatalar.append(f"{yer}: A Soru no boş")
            continue
        if (test, a) in gorulen_a:
            hatalar.append(f"{yer}: {test} A {a} ikinci kez eşlenmiş ({gorulen_a[(test, a)]})")
        gorulen_a[(test, a)] = yer
        if b is None:
            if "bulunamadı" not in durum:
                hatalar.append(f"{yer}: {test} A {a} için B Soru no boş, Durum “Bulunamadı” değil")
        else:
            if (test, b) in gorulen_b:
                hatalar.append(f"{yer}: {test} B {b} iki A sorusuna verilmiş ({gorulen_b[(test, b)]})")
            gorulen_b[(test, b)] = yer
        if (test, a) in ana and sira != ana[(test, a)]:
            hatalar.append(f"{yer}: {test} A {a} Sıra {sira}, ana tabloda {ana[(test, a)]}")

    testler = {t for t, _ in ana} | {t for t, _ in gorulen_a}
    for t in sorted(testler):
        a_set = {n for tt, n in gorulen_a if tt == t}
        b_set = {n for tt, n in gorulen_b if tt == t}
        ana_set = {n for tt, n in ana if tt == t}
        if ana_set - a_set:
            hatalar.append(f"{t}: kitapçık tablosunda olmayan A soruları {sorted(ana_set - a_set)}")
        if b_set - a_set:
            hatalar.append(f"{t}: A'da karşılığı olmayan B numaraları {sorted(b_set - a_set)}")
        if a_set - b_set:
            hatalar.append(f"{t}: hiçbir A sorusuna verilmemiş B numaraları {sorted(a_set - b_set)}")
    return len(kitapcik), hatalar


def main(yollar):
    if not yollar:
        print(__doc__)
        return 2
    kayitlar, kod_sira = kaynak_yukle()
    toplam_hata = 0
    for yol in yollar:
        adet, hatalar, bilgiler = denetle(yol, kayitlar, kod_sira)
        print(f"{yol}: {adet} Sıra satırı, {len(hatalar)} sorun, {len(bilgiler)} kod notu")
        for h in hatalar:
            print("  " + h)
        for b in bilgiler:
            print("  (bilgi) " + b)
        toplam_hata += len(hatalar)
        k_adet, k_hatalar = kitapcik_denetle(yol)
        if k_adet:
            print(f"  Kitapçık eşleşmesi: {k_adet} satır, {len(k_hatalar)} sorun")
            for h in k_hatalar:
                print("    " + h)
            toplam_hata += len(k_hatalar)
    return 1 if toplam_hata else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
