Sunucu Ubuntu 22.04 http://toccoapp.cloud:2002/ üzerinden canlı bir şekilde görülebilir (Verdiğiniz görevden anladığım kadarıyla bu şekilde bir yol izledim.)
1- Altyapı: https://github.com/TareqAlqutami/rtmp-hls-server
2- Litespeed panel üzerindeki docker yardımcısı modülü ile kuruldu.
3- Kodun sunucuya deploy edilmesi:
3.1 Virtual enviroment oluştur
3.2 Flask ve requests kütüphaneleri yüklenir.
3.3 Sunucuda servis aç
4- Test et: her 10 saniyede bir overlaydaki text random name generator üzerinden gelen bir ad soyad ile overlay oluşturduluğunu gör (biraz gecikme var)

Görevde localhost için dense de ben canlıda görülebilmesi için de kendime ait bir sunucuya çektim.
İYİ ÇALIŞMALAR
Oğuz Can Kısa