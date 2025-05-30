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


    match x:
        case "1":

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


        case "2":
            print("silmek istediğiniz kitabın bilgilerini giriniz")
            while True:
                silinisbn = input("kitabın isbn no'sunu giriniz")
                for b in mainkitaplar:
                    if silinisbn == b["isbn"]:
                        print("bulundu")
                        sil = {"ad": b["ad"], "tarih": b["tarih"], "isbn": b["isbn"]}
                        if sil in mainkitaplar:
                            mainkitaplar.remove(sil)
                            print("Kitap başarıyla silindi.")
                        else:
                            print("Bu bilgilerle eşleşen bir kitap bulunamadı.")
                        with open("kitaplar.json", "w") as f:
                            json.dump(mainkitaplar, f)
                        break
                    else:
                        print("İsbn hatalı")
                break

        case "3":
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
        case "4":
            break













