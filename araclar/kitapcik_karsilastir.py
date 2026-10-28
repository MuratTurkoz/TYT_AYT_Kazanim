"""Model çıktısındaki A/B kitapçık eşleşmesini referans tabloyla karşılaştırır.

Kullanım:
    python araclar/kitapcik_karsilastir.py <çıktı.xlsx | çıktı.md> <referans.md>

Her iki dosyada başlığında "Test", "A Soru no" ve "B Soru no" olan satırlar
okunur. Test adları anahtar sözcükle eşlenir (türkçe, sosyal, matematik, fen).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sira_kod_dogrula import md_tablolari, norm, sira_oku, sutun  # noqa: E402

TESTLER = ("türkçe", "sosyal", "matematik", "fen")


def test_adi(deger):
    s = norm(deger or "").lower()
    return next((t for t in TESTLER if t in s), s)


def satirlar(yol):
    if yol.lower().endswith(".xlsx"):
        import openpyxl

        kitap = openpyxl.load_workbook(yol, read_only=True, data_only=True)
        for sayfa in kitap:
            baslik = None
            for satir in sayfa.iter_rows(values_only=True):
                hucreler = list(satir)
                if baslik is None:
                    aday = [str(h or "").strip().lower() for h in hucreler]
                    if "a soru no" in aday and "b soru no" in aday:
                        baslik = aday
                    continue
                yield baslik, hucreler
    else:
        for _, baslik, hucreler in md_tablolari(yol):
            yield baslik, hucreler


def eslesme_oku(yol):
    sonuc = {}
    for baslik, hucreler in satirlar(yol):
        ai = sutun(baslik, lambda h: h == "a soru no")
        bi = sutun(baslik, lambda h: h == "b soru no")
        ti = sutun(baslik, lambda h: h == "test")
        if None in (ai, bi, ti):
            continue
        a = sira_oku(hucreler[ai]) if ai < len(hucreler) else None
        if a is None:
            continue
        b = sira_oku(hucreler[bi]) if bi < len(hucreler) else None
        sonuc[(test_adi(hucreler[ti]), a)] = b
    return sonuc


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    cikti, ref = eslesme_oku(argv[0]), eslesme_oku(argv[1])
    # Test bazlı çıktıda yalnızca dosyadaki testler karşılaştırılır.
    testler = {t for t, _ in cikti}
    ref = {k: v for k, v in ref.items() if k[0] in testler}
    print("Karşılaştırılan testler: " + ", ".join(sorted(testler)))
    dogru, hatalar = 0, []
    for anahtar in sorted(ref):
        if anahtar not in cikti:
            hatalar.append(f"{anahtar[0]} A {anahtar[1]}: çıktıda yok (doğrusu B {ref[anahtar]})")
        elif cikti[anahtar] != ref[anahtar]:
            hatalar.append(f"{anahtar[0]} A {anahtar[1]}: çıktı B {cikti[anahtar]}, doğrusu B {ref[anahtar]}")
        else:
            dogru += 1
    fazla = sorted(set(cikti) - set(ref))
    print(f"{dogru}/{len(ref)} eşleşme referansla aynı, {len(hatalar)} fark, {len(fazla)} referansta olmayan satır")
    for h in hatalar:
        print("  " + h)
    for t, a in fazla:
        print(f"  {t} A {a}: referansta yok")
    return 1 if hatalar or fazla else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
