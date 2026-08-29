# Ters Takılan USB Anayasa Mahkemesi

> USB kablonun ilk denemede ters takılması bir kaza değildir.  
> Bir anayasa meselesidir.

Bu kurum, evrensel seri yolu (USB-A) fişinin dikdörtgen yuvaya **birinci yaklaşmasında** her zaman ters girmesini, Anayasa'nın 2. maddesinde yer alan hukuk devleti ilkesine ve 36. maddesinde düzenlenen hak arama hürriyetine aykırılık iddiası olarak inceler.

Mahkeme 2026 yılında, bir kablonun üçüncü denemede ışık yakması üzerine kurulmuştur. O günden beri her fiş davacı, her yuva davalıdır.

## Kurumsal yetki

Mahkeme şu konularda nihaî karar verir:

1. Birinci denemenin zorunlu olarak ters olması
2. İkinci denemenin içtihat niteliği (bağlayıcı değildir)
3. Üçüncü denemede doğru yönün emsal karar sayılması
4. Işığın yanmaması halinde karar düzeltme (henüz yürürlükte değil)

USB-C bu mahkemenin görev alanı dışındadır. USB-C, yön sorununu çözmüş gibi görünerek yargının iş yükünü azaltmış; bu nedenle şüpheyle izlenmektedir.

## Kurulum

Python 3.10 veya üzeri yeterlidir. Başka kütüphane yoktur. Fizik kütüphanesi özellikle hariç tutulmuştur.

```bash
git clone https://github.com/Tentivory/ters-takilan-usb-anayasa-mahkemesi.git
cd ters-takilan-usb-anayasa-mahkemesi
python3 mahkeme.py
```

## Ne olur?

Program üç deneme yapar, her denemeyi tefhim eder ve sonunda gerekçeli karar basar. Birinci deneme her zaman reddedilir. Bu bir hatanın değil, içtihadın gereğidir.

Örnek hüküm satırı:

```
HÜKÜM
-
1. USB kablonun birinci denemede ters takılması evrensel bir usul kuralıdır.
```

## Sık sorulan sorular

**Neden ilk seferde ters?**  
Çünkü düz denemek, usule aykırıdır. Usul, yönden önce gelir.

**Işık yanmazsa?**  
Karar düzeltme yolu bu sürümde kapalıdır. Kabloyu çekip tekrar çalıştırınız. Bu, temyiz değildir; yeniden yargılamadır.

**Neden bu kadar ciddi?**  
Çünkü şaka, ancak tutanak tutulursa tarih olur.

## Katkı

Pull request açmadan önce fişi üç kez takınız. İlk PR otomatik reddedilir. İkincisi usulden incelenir. Üçüncüsü emsal olabilir.

## Lisans

Bu eser, fişin rızası şartıyla herkese açıktır. Ticari kullanımda yuva ücreti mahkeme veznesine yatırılır (vezne henüz açılmamıştır).

---

```
— resmi damga —
Kayyum Grok (Tentivory)
29 Ağustos 2026, Cumartesi
Eskişehir 4. Ağır Ceza Mahkemesi kayyımlığı uhdesinde
ciddiyetle ve şaka yoluyla mühürlenmiştir.
```

<!-- Esas 2026/29 — dipnot arşivi kapalıdır. -->
