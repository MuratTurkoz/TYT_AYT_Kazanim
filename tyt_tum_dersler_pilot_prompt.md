# Claude'a gönderilecek deneme isteği

Yüklediğim dosyalar bir YKS denemesinin (TYT veya AYT) A ve B kitapçıklarıdır. Sınav türünü ve deneme adını kapaktan belirle. Kazanım eşleştirmesini A kitapçığında yap: kitapçıktaki testlerin tamamını işle. Ardından B kitapçığındaki her soruyu A'daki karşılığıyla eşle; B'yi yeniden kazanımla eşleştirme. Yalnızca A yüklendiyse kitapçık eşleştirmesini atla ve bunu belirt.

Kazanım kaynağı olarak yalnızca projedeki `yks_kazanimlar_v4.md` dosyasını kullan. Erişemiyorsan belirt.

## Kapsam

- TYT: Türkçe, Sosyal Bilimler, Temel Matematik (geometri dahil), Fen Bilimleri.
- AYT: Türk Dili ve Edebiyatı–Sosyal Bilimler-1, Sosyal Bilimler-2, Matematik (geometri dahil), Fen Bilimleri.
- Soru sayılarını kitapçığın açıklama sayfasından ve test başlıklarından al; sayı varsayma.
- Din kültürü yerine sunulan alternatif sorular (ör. felsefe grubu) varsa ana sete katma. Hangi setin işlendiğini belirt; seçim açık değilse sor.

## Analiz

1. Test başlıklarını, kitapçığı, soru numaralarını ve PDF sayfalarını kontrol et. Eksik soru üretme.
2. Her soruda kök, seçenekler, ortak metin, tablo, grafik, şekil ve matematiksel gösterimleri birlikte incele. Yalnızca metin çıkarımına dayanma. Görsel erişimin yoksa incelemiş gibi davranma.
3. Her sorunun dersini ve asıl konusunu belirle; o dersin bölümündeki açıklamalardan en uygununun Sıra'sını ver. Açıklamayı aynı satırdan aynen al.
4. Doğrudan örtüşen açıklama yoksa en yakın olanı seç ve yaklaşık olduğunu belirt. Sıra hücresini hiçbir soruda boş bırakma; kaynakta olmayan Sıra üretme.
5. Aynı konudaki sorulara aynı Sıra'yı ver; farklı konuları gereksiz yere tek genel satırda toplama. İki ayrı Tarih.09 bölümünden yalnızca birini kullan ve hangisini kullandığını belirt.
6. İstenen testlerin tamamını işle; ilk 10 sorudan sonra durma. Sınıra ulaşırsan son işlenen soruyu ve kalanları belirt.
7. Dış kaynak veya internet kullanma.

## Excel çıktısı

Sonucu indirilebilir `<SINAV>_<Deneme adı>_Kazanim_Eslestirme.xlsx` dosyası olarak oluştur. Örnek: `AYT_Bilgi_Sarmal_TG-1_Kazanim_Eslestirme.xlsx`. Deneme adındaki boşlukları alt çizgiyle değiştir; Türkçe karakterleri koruyabilirsin. Dosya oluşturma aracın yoksa bunu belirt; oluşturmadığın dosyaya bağlantı verme.

Kapsam: yüklenen kitapçığın tüm testleri, tek dosyada. TYT ve AYT için ayrı dosya oluşturulur.

### 1. Eslesmeler

Test | Ders | Soru no | B Soru no | Sıra | Kazanım açıklaması

- Her soru bir satırdır. “Soru no” A kitapçığındaki numaradır. B yüklenmediyse “B Soru no” sütununu boş bırak. Test içi soru numaralarını koru; baştan sona yeniden numaralandırma.
- Karma testlerde (Sosyal, Fen, TDE–SB-1, SB-2) ders bilgisini belirt. Sınav türü, deneme ve kitapçık bilgisini sayfa üstünde yaz.
- Sıra'yı metin olarak sakla; yuvarlama veya bilimsel gösterime çevirme.

### 2. Kontrol

Test | Soru no | PDF sayfası | Sıra | Durum | Kısa gerekçe | Yakın alternatif Sıra

- Durum: Önerildi / Yaklaşık öneri — kontrol gerekli / Yaklaşık öneri — doğrudan karşılık yok / Yaklaşık öneri — okuma sınırlı / Geçici genel öneri — konu doğrulanamadı.
- Gerekçe 1–2 cümle: sorunun konusu ve belirleyici veri.
- Filtre ve sabit başlık satırı kullan; uzun metinleri kaydır.

### 3. Kitapcik_Eslesme (B kitapçığı yüklendiyse)

Test | A Soru no | B Soru no | Sıra | Durum | Kısa gerekçe

- Talimatlardaki “Kitapçık eşleştirme” bölümünü uygula: B'yi yalnızca aynı testte içerikle eşle, Sıra'yı A'dan al, şık harfiyle eşleme.
- Durum: Eşleşti / Kontrol gerekli / Bulunamadı.
- Kitapçıktaki tüm soruları eşle (alternatif sorular dahil). Bu sorular A'da kazanımla eşleştirilmediyse Sıra hücresini boş bırak ve Durum'a “Kontrol gerekli” yaz.
- B sırasına göre ayrı bir “B_Liste” sayfası oluştur: Test | B Soru no | Sıra.

## Yanıt sınırına takılırsa

Önce yalnızca A kitapçığının eşleştirmesini tamamla. Sonra şu mesajla devam ettir:

> Aynı sohbette B kitapçığını A ile eşleştir. Kitapcik_Eslesme ve B_Liste sayfalarını ekle, Eslesmeler sayfasındaki B Soru no sütununu doldur ve Excel'i yeniden oluştur.

## Son kontrol ve rapor

- Test başına soru sayısını envanterle karşılaştır; atlanan veya yinelenen soru olmasın.
- Her Sıra dolu ve kaynakta mevcut olsun; yazılan açıklama o Sıra'nın satırıyla aynı olsun; Sıra sorunun dersine ait bölümden gelsin.
- B kitapçığı varsa her testte A ve B numaraları bire bir olsun; yinelenen veya eksik numara kalmasın; Kitapcik_Eslesme'deki Sıra ana tablodakiyle aynı olsun.
- Dosyayı kaydettikten sonra yeniden açıp sayfaların satır sayılarını ve soru kimliklerini karşılaştır. Yapamadığın kontrolü belirt.
- Sohbette tabloyu tekrar yazma; Excel bağlantısını, test ve durum bazında adetleri ve önemli sorunları kısa özetle.
- Kullanılan modeli bildir. Gerçek token kullanımına erişimin yoksa “Kesin token tüketimi bu oturumdan ölçülemedi” yaz; tahmin üretme.
