# Face Target Project from Arduino Uno


## Proje Hakkında

Bu proje, yüz tanıma teknolojisi kullanarak hedefli bir kişiyi tanıma ve takip etme amacını taşımaktadır. Proje, canlı video akışı veya kaydedilmiş videolar üzerinde çalışabilir. Hedefli kişiyi tespit eder ve izlerken, yüz tanıma algoritması kullanarak onu tanıyabilir. Arduino Uno İle entegre olarak servo motorlar ile algılanan yüzü otomatik olarak takip ederek hareket gerçekleştirir.

## Özellikler

- Hedefli kişiyi tanıma ve takip etme yeteneği
- Yüz tanıma algoritması kullanma
- Canlı video akışından yüz verilerini analiz etme
- Kamera veya video kaynağından yüzü izleme ve takip etme
- Algılanan yüzü servo motorlar yardımıyla takip ederek hedef takibi gerçekleştirme 

## Kurulum ve Kullanım

### Gereksinimler

- Python 3.x
- OpenCV Kütüphanesi
- Arduino Uno
- Servo Motor
- Arduino Uno Sensor Shield
- Harici Kamera(" İsteğe Bağlı Laptopta bulunan dahili kamera için de çalışmaya uygundur")
- 3D Baskı("İsteğe Bağlı servo motorları sabitleyecek bir düzenek kullanılabilir basit tahta yada plastik gibi...")
- 

### Kurulum

1. Depoyu yerel makinenize klonlayın:

   ```bash
   git clone https://github.com/MelihOzaslan01/face-target-project.git` 

Save to grepper

2.  Proje klasörüne gidin:
    
    bashCopy code
    
    `cd face-target-project` 
    
3.  Gerekli bağımlılıkları yükleyin:
    
    bashCopy code
    
    `pip install -r requirements.txt` 
    

### Kullanım

1.  Proje klasöründe aşağıdaki komutu çalıştırarak projeyi başlatın:
    
    bashCopy code
    
    `python main.py` 
    
2.  Proje çalıştırıldığında, canlı video akışı veya kaydedilmiş bir video açılacaktır. Hedefli kişinin yüzünü doğru bir şekilde çerçeveleyin ve takip işlemini başlatın. Projeyi kullanırken veya test ederken dikkate almanız gereken ek bilgileri buraya ekleyin.
    

## Katkıda Bulunma

1.  Bu projeye katkıda bulunmak için bir dal oluşturun:
    
    bashCopy code
    
    `git checkout -b feature/YeniOzellik` 
    
2.  Yapmak istediğiniz değişiklikleri yapın ve bunları taahhüt edin:
    
    bashCopy code
    
    `git commit -am 'Yeni özellik: Açıklama'` 
    
3.  Dalınızı ana depoya gönderin:
    
    bashCopy code
    
    `git push origin feature/YeniOzellik` 
    
4.  Bir Birleştirme İsteği oluşturun ve incelemeye gönderin.
    

![1](https://drive.google.com/file/d/1pqhzt_NdJyfY9T10vRloNlqo43q4vp2H/view?usp=drive_link)
![2](https://drive.google.com/file/d/1H7GIEkHdvoVg167-Dv87j5a4Vpw2xTUW/view?usp=drive_link)

## İletişim

E-posta: melihozaslan01@gmail.com

Proje bağlantısı:  https://github.com/MelihOzaslan01/face-target-project
