# TYT–AYT Soru ve Kazanım Eşleştirme

TYT/AYT deneme sorularını, okulun kazanım listesindeki uygun satırın **Sıra** numarasıyla eşleştirmek için hazırlanmış bir Claude Project kurulumu.

Öğretmenler her denemeden önce soruları tek tek inceleyip okul sistemine kazanım Sıra'sını giriyor. Bu proje, Claude'un her soru için kontrol edilebilir bir Sıra önerisi üretmesini sağlar. Sonuç bir Excel dosyasıdır. **Öneriler onay değildir; nihai karar branş öğretmenine aittir.**

## Nasıl çalışır?

1. Denemenin A (ve varsa B) kitapçık PDF'leri Claude'a yüklenir.
2. Claude her soruyu okur, sorunun ölçtüğü konuyu belirler ve kazanım kaynağındaki en uygun açıklamanın Sıra'sını verir.
3. B kitapçığındaki sorular içeriklerine göre A'daki karşılıklarıyla eşlenir ve A'nın Sıra'sını alır.
4. Sonuç Excel olarak indirilir. Excel'deki sayfalar:
   - `Eslesmeler`: Test, Ders, Soru no, B Soru no, Sıra, Kazanım açıklaması
   - `Kontrol`: Durum, kısa gerekçe, yakın alternatif Sıra
   - `Kitapcik_Eslesme` ve `B_Liste`: A–B karşılıkları

Eşleştirmede yalnızca **Sıra** ve **kazanım açıklaması** kullanılır. Kazanım kodu ve derinlik seçim ölçütü değildir.

## Claude Project kurulumu

İki kurulum seçeneği var. Ücretli planlarda (Pro, Max, Team) **A** daha basittir. Ücretsiz planda veya proje bilgi kotası sorun çıkarırsa **B**'yi kullan.

### A) Tek kaynak dosyasıyla kurulum

1. [claude.ai](https://claude.ai) adresinde **Projects → Create project** yolunu izle ve projeye bir ad ver (örneğin “Kazanım Eşleştirme”).
2. [talimatlar.md](talimatlar.md) dosyasının içeriğini kopyala ve projenin **Instructions** (Talimatlar) alanına yapıştır.
3. Projenin **Files** (Dosyalar) bölümüne şu iki dosyayı ekle:
   - [baglam.md](baglam.md): amaç, alanlar ve onaylı kararlar
   - [yks_kazanimlar_v4.md](yks_kazanimlar_v4.md): kazanım kaynağı (TYT + AYT, 16 ders, 1976 satır)
4. **Ayarlar → Özellikler** altında dosya oluşturma / kod çalıştırma özelliğinin açık olduğundan emin ol. Excel çıktısı için bu gerekir.

Her deneme için yeni sohbet aç, A ve B kitapçık PDF'lerini ekle ve [istek_tum_testler.md](istek_tum_testler.md) dosyasının içeriğini gönder.

### B) Ders bazlı dosyalarla kurulum

Kaynak ders ders bölünmüştür ve her test için hazır istek metinleri vardır.

1. Yeni bir proje oluştur.
2. [ucretsiz/proje/](ucretsiz/proje/) klasöründeki **12 dosyanın tamamını** projenin **Files** bölümüne ekle (`talimatlar.md`, `baglam.md` ve 10 adet `kaynak_<ders>.md`).
3. **Instructions** alanı varsa [ucretsiz/proje/talimatlar.md](ucretsiz/proje/talimatlar.md) içeriğini oraya da yapıştır. Kök dizindeki `talimatlar.md` dosyasını bu kurulumda **kullanma**: o dosya projede olmayan `yks_kazanimlar_v4.md` kaynağını arar.

Adım adım kullanım ve sorun giderme için [ucretsiz/README.md](ucretsiz/README.md) dosyasına bak.

## Kullanım

Her deneme (veya her test) için proje içinde **yeni bir sohbet** aç ve denemenin **A** ve **B** kitapçık PDF'lerini ekle. Ardından kurulumuna uygun istek metnini kopyalayıp gönder:

- **A kurulumu:** [istek_tum_testler.md](istek_tum_testler.md). Tek seferde tüm testleri işler ve tek Excel üretir.
- **B kurulumu:** [ucretsiz/istekler/](ucretsiz/istekler/) klasöründeki ilgili dosya:

| Test | İstek dosyası |
|---|---|
| Tüm testler tek seferde | [00_Tum_Testler.md](ucretsiz/istekler/00_Tum_Testler.md) |
| TYT Türkçe | [01_TYT_Turkce.md](ucretsiz/istekler/01_TYT_Turkce.md) |
| TYT Sosyal Bilimler | [02_TYT_Sosyal.md](ucretsiz/istekler/02_TYT_Sosyal.md) |
| TYT Temel Matematik | [03_TYT_Temel_Matematik.md](ucretsiz/istekler/03_TYT_Temel_Matematik.md) |
| TYT Fen Bilimleri | [04_TYT_Fen.md](ucretsiz/istekler/04_TYT_Fen.md) |
| AYT TDE–Sosyal Bilimler-1 | [05_AYT_TDE_SB1.md](ucretsiz/istekler/05_AYT_TDE_SB1.md) |
| AYT Sosyal Bilimler-2 | [06_AYT_SB2.md](ucretsiz/istekler/06_AYT_SB2.md) |
| AYT Matematik | [07_AYT_Matematik.md](ucretsiz/istekler/07_AYT_Matematik.md) |
| AYT Fen Bilimleri | [08_AYT_Fen.md](ucretsiz/istekler/08_AYT_Fen.md) |

`ucretsiz/istekler/` dosyaları B kurulumundaki `kaynak_<ders>.md` adlarını kullanır; A kurulumunda bunları değil `istek_tum_testler.md` dosyasını kullan.

Yanıt yarıda kalırsa aynı sohbete `devam` yaz. Tüm testler tek seferde bitmezse testleri ayrı sohbetlerde (01–08) işle. PDF çok büyükse [araclar/pdf_bol.py](araclar/pdf_bol.py) ile testlere böl.

## Klasör yapısı

| Yol | İçerik |
|---|---|
| [talimatlar.md](talimatlar.md) | Claude'un uyduğu eşleştirme kuralları |
| [baglam.md](baglam.md) | Proje amacı, alan tanımları ve onaylı kararlar (K-001…) |
| [yks_kazanimlar_v4.md](yks_kazanimlar_v4.md) | TYT/AYT kazanım kaynağı (Sıra \| açıklama) |
| [istek_tum_testler.md](istek_tum_testler.md) | A kurulumunda sohbete gönderilen istek metni |
| [kazanimlar/](kazanimlar/) | Tüm branşların ham kazanım aktarımı (`tum_kazanimlar.json` ve ders bazlı `.md` dosyaları) |
| [ucretsiz/](ucretsiz/) | Ders bazlı kurulum dosyaları ve test istekleri |
| [referans/](referans/) | Model çıktısını denetlemek için elle hazırlanmış A/B kitapçık karşılıkları |
| [araclar/](araclar/) | Kaynak üretme ve çıktı doğrulama betikleri |

## Araçlar

Python 3 gerekir. `pdf_bol.py` ve `.xlsx` okuyan betikler için:

```bash
pip install pypdf openpyxl
```

| Betik | Ne yapar |
|---|---|
| `python araclar/kaynak_olustur.py yks_kazanimlar_v4.md` | Kazanım kaynağını `kazanimlar/tum_kazanimlar.json` üzerinden yeniden üretir |
| `python araclar/ucretsiz_olustur.py` | `ucretsiz/` klasöründeki ders dosyalarını ve istekleri üretir |
| `python araclar/sira_kod_dogrula.py <çıktı.xlsx>` | Claude'un çıktısını denetler: Sıra'lar dolu mu, kaynakta var mı, açıklamalar tutuyor mu, A–B eşleşmesi bire bir mi |
| `python araclar/kitapcik_karsilastir.py <çıktı.xlsx> referans/TG1_kitapcik_AB.md` | A–B kitapçık eşleşmesini elle hazırlanmış referansla karşılaştırır |
| `python araclar/pdf_bol.py <kitapçık.pdf> Turkce=3-19 Sosyal=20-26 ...` | Deneme PDF'ini test bazlı parçalara böler |

## Notlar

- Kazanım verisi okulun `ALL BRANŞLAR KAZANIM.xlsx` dosyasından aktarılmış ve Sıra bazında Excel ile doğrulanmıştır. Başka bir okulun listesinde Sıra değerleri farklı olabilir.
- Deneme kitapçıkları yayınevlerine aittir ve bu depoda yer almaz.
- Talimat veya kaynak dosyalarını değiştirirsen, Claude'un güncel hali görmesi için dosyaları projeye yeniden yükle.
