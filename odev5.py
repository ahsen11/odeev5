# Bankamatik Uygulaması
# Hesap bilgileri tutulacak. (dictionary)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.



hesap={'bakiye':1500,'ek bakiye':1000}

def menu():
    print("------X Bankasına Hoş Geldiniz------")
    print("1-Para Çekme")
    print("2-Bakiye Sorgulama")
    print("3-Para Yatırma")
    print("4-Çıkış")
    islem=input("Yapmak istediğiniz işlemi seçiniz: ")
    if islem=="1":
        paraCekme()
    elif islem=="2":
        bakiyeSorgulama()
    elif islem=="3":
        paraYatirma()
    elif islem=="4":
        print("Çıkışınız gerçekleşmiştir")
        exit()
    else:
        print("Geçersiz işlem. Lütfen tekrar deneyiniz.")
        menu()

def paraCekme():
    cekilecekPara=float(input("Çekmek istediğiniz miktar: "))
    if cekilecekPara<=hesap["bakiye"]:
        hesap["bakiye"]-=cekilecekPara
        print(f"{cekilecekPara} TL başarıyla çekilmiştir.Güncel bakiye:{hesap['bakiye']}")
    elif cekilecekPara<=hesap['bakiye']+hesap['ek bakiye']:
        onay=input("Hesabınızdaki para yetersizdir. Ek hesabınızdan çekmek ister misiniz?(e/h):")
        if onay=="e":
            toplam_hesap=hesap["bakiye"]+hesap["ek bakiye"]
            hesap["ek bakiye"]-=(toplam_hesap-cekilecekPara)
            hesap["bakiye"]=0
            print(f"{cekilecekPara} TL başarıyla çekilmiştir.Ek hesabınızda kalan para:{hesap['ek bakiye']}")
        elif "h":
            print("İşleminiz iptal edilmiştir.")

        hesap["bakiye"]=0
        hesap["ek bakiye"]-=(cekilecekPara-hesap["bakiye"])
        print(f"{cekilecekPara} TL başarıyla çekilmiştir.Ek hesabınızda kalan miktar:{hesap['ek bakiye']}")
    else:
        print("Hesabınızda yeterli miktarda para yoktur.")
    menu()
def bakiyeSorgulama():
    print(f"Hesabınızda {hesap['bakiye']} TL,ek hesabınızda {hesap['ek bakiye']} TL vardır.")
    menu()
def paraYatirma():
    yatirilacakPara=float(input("Yatırmak istediğiniz miktar:"))
    hesap['bakiye']+=yatirilacakPara
    print(f"Para yatırma işlemi başarıyla tamamlandı.Güncel bakiye:{hesap['bakiye']}")
    menu()

menu()