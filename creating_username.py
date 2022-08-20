import sys
import random


def kullanıcıadiOlusturucu(sayi):
    data=[]
    kelime1 = random.choice(x)
    kelime2 = random.choice(x)
    if not kelime1==kelime2:
        kullaniciadi= kelime1 + kelime2 +sayi
        if not kullaniciadi in data:
            data.append(kullaniciadi)
        print(kullaniciadi)

print("Merhaba ben Jeriko. Size Kullanıcı adı olusturmak için görevlendirildim. Hazırsanız başlayalım.")

while True:
    sayı1=' '
    seçenek = input("Kendi verdiğiniz verilerle kullanıcı adı oluşturmak için 1, Random kullanıcı adı oluşturmak için 2 yazmanız yeterli.\n")
    if (seçenek == "1"):
        veri = input("Sevdiğiniz kelime ve sayıları giriniz. ")
        x=[]
        x.append(veri)
        x = veri.split()
        kullanıcıadiOlusturucu(sayı1)
        break
    elif (seçenek =="2"):
        x = ['peri','rüya','gece','gündüz','kar','ateş','mavi','ejder','zaman','kaptan','sessiz']
        nolu=input("Kullanıcı adınızda sayı bulundurmak ister misiniz? (Cevabınız evetse E ,hayırsa H yazmanız yeterli)")
        if ((nolu=="e") or (nolu=="E")):
            y=['65','44','22','13','8','25','97','654','01','83','917']
            sayı1=random.choice(y)
            kullanıcıadiOlusturucu(sayı1)
        else:
            kullanıcıadiOlusturucu(sayı1)
        break
    else:
        print("Hatalı tuşlama.")