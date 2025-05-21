import json
import random
from _datetime import datetime

try:
    with open("kitaplar.json") as f:
        mainkitaplar = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):

    mainkitaplar = []

while True :
    print("Kitap kayıt sistemi \n 1. Kitap ekle \n 2. kitap sil \n 3. kayıtlı kitapları görüntüle \n 4. çıkış ")
    x = input("\nyapmak istediğiniz işlemi seçiniz")


    if x == "1" :

        with open("kitaplar.json", "w") as f:
            json.dump(mainkitaplar, f)
        ad = input("ad giriniz")

        isbn = random.randint(1000000,9999999)
        isbn = str(isbn)

        while True:
            tarih = input("Tarihi 'gg/aa/yyyy' formatında girin: ")
            try:
                tarih = datetime.strptime(tarih, "%d/%m/%Y")
                break
            except ValueError:
                print("Lütfen gg/aa/yyyy biçiminde tekrar girin.")
        tarihstr = tarih.strftime("%d/%m/%Y")

        kitaplar = {"ad": ad ,"tarih": tarihstr,"isbn" :isbn}
        mainkitaplar.append(kitaplar)
        with open("kitaplar.json", "w") as f:
            json.dump(mainkitaplar, f)
        print("kitap kaydedildi")


    if x == "2" :
        print("silmek istediğiniz kitabın bilgilerini giriniz")
        while True:
            silinenad = input("kitabın adını giriniz")
            if silinenad in mainkitaplar:
                print("bulundu")
                break
            else:
                print("Kitap bilgilerini doğru giriniz")

        while True:
            silinentarih = input("Tarihi 'gg/aa/yyyy' formatında girin: ")
            try:
                silinentarih = datetime.strptime(silinentarih, "%d/%m/%Y")
                break
            except ValueError:
                print("Lütfen gg/aa/yyyy biçiminde tekrar girin.")
        silinentarihstr = silinentarih.strftime("%d/%m/%Y")

        silinenisbn = input("kitabın isbn no sunu giriniz")
        while True:
            silinisbn = input("kitabın adını giriniz")
            if silinisbn in mainkitaplar:
                print("bulundu")
                break
            else:
                print("İsbn hatalı")

        sil = {"ad" : silinenad , "tarih" : silinentarihstr , "isbn" :silinenisbn }
        if sil in mainkitaplar:
            mainkitaplar.remove(sil)
            print("Kitap başarıyla silindi.")
        else:
            print("Bu bilgilerle eşleşen bir kitap bulunamadı.")
        with open("kitaplar.json", "w") as f:
            json.dump(mainkitaplar, f)


    if x == "3":
        while True:
            arananad = input("kitabın adını giriniz")
            for a in mainkitaplar:
                if arananad == a["ad"]:
                    print("kitap bulundu\n")
                    print("kitap adı:",a["ad"],"\n","yazılma tarihi:",a["tarih"],"\n","kitap isbn no:",a["isbn"],"\n")
                    break
            else:
                print("Kitap bilgilerini doğru giriniz")
                continue
            break
    if x == "4":
        break












