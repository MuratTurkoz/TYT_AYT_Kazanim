"""Deneme PDF'ini test bazlı parçalara böler.

Kullanım:
    python araclar/pdf_bol.py <kitapçık.pdf> <Ad=başlangıç-bitiş> [...]

Örnek (Bilgi Sarmal TG-1, A ve B aynı sayfa düzeninde):
    python araclar/pdf_bol.py "TG-1 - A.pdf" Turkce=3-19 Sosyal=20-26 Matematik=27-39 Fen=40-47

Sayfa numaraları PDF sırasıdır (ilk sayfa 1). Çıktılar kitapçığın yanına
"<kitapçık adı>_<Ad>.pdf" olarak yazılır.
"""

import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    girdi = Path(argv[0])
    okuyucu = PdfReader(str(girdi))
    toplam = len(okuyucu.pages)
    for parca in argv[1:]:
        ad, _, aralik = parca.partition("=")
        bas, _, son = aralik.partition("-")
        bas, son = int(bas), int(son or bas)
        if not 1 <= bas <= son <= toplam:
            print(f"{parca}: geçersiz aralık (PDF {toplam} sayfa)")
            return 1
        yazici = PdfWriter()
        for i in range(bas - 1, son):
            yazici.add_page(okuyucu.pages[i])
        cikti = girdi.with_name(f"{girdi.stem}_{ad}.pdf")
        with open(cikti, "wb") as f:
            yazici.write(f)
        print(f"{cikti.name}: sayfa {bas}-{son}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
