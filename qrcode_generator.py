import qrcode
import random
import os

def qrcodeoluştur():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(x)
    qr.make(fit=True)
    img = qr.make_image(fill_color = n, back_color = m)
    img.save(y)
    img.show()


print("Merhaba ben Jeriko.")
print("QR kod oluşturucuya hoş geldiniz.")
menusec=input("Rastgele QR kod oluşturmak için 1, kendi QR kodunuzu oluşturmak için 2 yazmanız yeterlidir:")
os.system('CLS')
urldata = ['https://translate.google.com/?hl=tr','https://altinkariyerakademi.com.tr','https://www.youtube.com','https://www.instagram.com', \
    'https://twitter.com/i/flow/login?input_flow_data=%7B"requested_variant"%3A"eyJsYW5nIjoidHIifQ%3D%3D"%7D','https://www.google.com.tr/?hl=tr']
pngdata = ['randomqrkod1','randomqrkod2','randomqr3']
renkdata=['pink','black','purple','blue','green','yellow','grey','orange','white']
if (menusec=="1"):
    x = random.choice(urldata)
    y = random.choice(pngdata)+".png"
    m = random.choice(renkdata)
    renkdata.remove(m)
    n=random.choice(renkdata)
    qrcodeoluştur()
elif(menusec=="2"):
    x=input("QR kodunu yapmak istediğiniz sayfanın url'sini giriniz:").lower()
    y=input("Oluşturduğunuz QR kodunu kaydetmek istediğiniz ismi yazınız:").lower()+".png"
    os.system('CLS')
    for j in range(2):
        a = 0
        for i in renkdata:
            a = a + 1
            print( a,".",i)
        if j == 0:
            m = renkdata[int(input("Arka plan için istediğiniz rengin numarasını belirtiniz."))-1]
            renkdata.remove(m)
        else:
            n = renkdata[int(input("Kutucuklar için istediğiniz rengin numarasını belirtiniz."))-1]
        os.system('CLS')
    qrcodeoluştur()
else:
    print("Herhangi bir girişte bulunmadınız.")

print("QR kodunuzu oluşturdunuz. Jeriko size iyi günler diler. :)")

