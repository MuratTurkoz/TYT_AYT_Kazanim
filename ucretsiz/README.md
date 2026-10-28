# Claude ücretsiz sürümde deneme — adım adım

## 1. Projeyi kur (bir kez)

1. claude.ai → **Projects** → **Create project** (ör. “Kazanım Eşleştirme”).
2. `proje` klasöründeki **12 dosyanın hepsini** projenin **Files** (Dosyalar) bölümüne ekle:
   - `talimatlar.md`, `baglam.md`
   - `kaynak_turkce.md`, `kaynak_edebiyat.md`, `kaynak_matematik.md`, `kaynak_tarih.md`, `kaynak_cografya.md`, `kaynak_felsefe.md`, `kaynak_din.md`, `kaynak_fizik.md`, `kaynak_kimya.md`, `kaynak_biyoloji.md`
3. Projede **Instructions** (Talimatlar) alanı görünüyorsa `talimatlar.md` içeriğini oraya da yapıştır. Görünmüyorsa geç.

## 2. Her test için yeni sohbet

Proje içinde **yeni sohbet** aç:

1. Denemenin **A** ve **B** PDF'lerini ekle.
2. `istekler` klasöründen o testin dosyasını aç, içeriğini kopyala, mesaj kutusuna yapıştır, gönder.

| Test | İstek dosyası |
|---|---|
| **Tüm testler tek seferde** (TYT veya AYT) | `00_Tum_Testler.md` |
| TYT Türkçe | `01_TYT_Turkce.md` |
| TYT Sosyal Bilimler | `02_TYT_Sosyal.md` |
| TYT Temel Matematik | `03_TYT_Temel_Matematik.md` |
| TYT Fen Bilimleri | `04_TYT_Fen.md` |
| AYT TDE–Sosyal Bilimler-1 | `05_AYT_TDE_SB1.md` |
| AYT Sosyal Bilimler-2 | `06_AYT_SB2.md` |
| AYT Matematik | `07_AYT_Matematik.md` |
| AYT Fen Bilimleri | `08_AYT_Fen.md` |

Önce `00_Tum_Testler.md` ile dene. Yarıda kalırsa `devam` yaz; yine de bitmezse yeni sohbetlerde test test (01–08) ilerle.

Claude bir Excel verir (ör. `AYT_<Deneme>_SB2_Kazanim_Eslestirme.xlsx`). İndir ve sakla.

## Takılırsa

- **Kota doldu / yanıt yarıda kaldı:** Bekle, aynı sohbete `devam` yaz.
- **PDF yüklenmiyor veya çok yavaş:** Tarayıcıda PDF'i aç → Yazdır → “PDF olarak kaydet” → yalnızca o testin sayfalarını seç; onu yükle.
- **Excel oluşmuyor:** Ayarlar → Özellikler'de dosya oluşturma / kod çalıştırma açık olmalı.
- **Proje dosyaları kotayı hızla dolduruyorsa:** Kullanmadığın sınavın dosyalarını kaldırabilirsin (ör. yalnızca TYT deniyorsan `kaynak_edebiyat.md`).

Excel'leri bana gönderirsen Sıra'ları ve A–B eşleşmesini kontrol ederim.
