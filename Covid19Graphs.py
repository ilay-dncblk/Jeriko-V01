import time
import matplotlib.pyplot as plt
import os

print("Merhaba ben Jeriko. Covid19 Veri Tabloları uygulamamıza hoş geldiniz.")

secenek=['Son 1 aylık haftalık vaka sayısı','Son 1 aylık haftalık vefat sayısı', 'Son 1 aylık haftalık iyileşen sayısı','Son 1 aylık toplam vaka sayısı', 'Son 1 aylık toplam vefat sayısı','12-13 Ağustos vaka ve vefat sayısı karsılastırma','13 Ağustos verileri','Uygulamadan çıkmak için herhangi bir tuşa basınız.']

a = 0
for i in secenek:
    a = a + 1
    print( a,".",i)
    time.sleep(1)
    
menusec=input("Görmek istediğiniz tablonun numarasını giriniz. : ")
os.system('CLS')

hva=['0','406.322','365.424','226.532','117.095','57.113']
hve=['0','337','157','96','31','25']
hi=['0','387.653','265.962','124.732','61.047','30.478']
tva=['','16.295.817','15.889.495','15.524.071','15.297.539','15.180.444']
tve=['','99.678','99.341','99.184','99.088','99.057']
g=['','25.08-01.09','18-24.08','11-17.08','04-10.08','27.07-03.08']
g2=['12.09.2022','13.09.2022']
hva2=['589 Mn', '598.770 B']
hve2=['6,43 Mn','6,432,727']
veri13=['0','598.770 B','6,432,727']
g3=['','vaka sayısı','vefat sayısı']

while True:

    if (menusec=="1"):
        plt.plot(g,hva,"r--")
        plt.suptitle("Son 1 aylık haftalık vaka sayısı")
        plt.ylabel("Aylık Vaka Sayısı")
        plt.xlabel("Günler")
        plt.show()
    
    elif(menusec=="2"):
        plt.plot(g,hve,"o--")
        plt.suptitle("Son 1 aylık haftalık vefat sayısı")
        plt.ylabel("Aylık Vefat Sayısı")
        plt.xlabel("Günler")
        plt.show()

    elif(menusec=="3"):
        plt.plot(g,hi,"b--")
        plt.suptitle("Son 1 aylık haftalık iyileşen sayısı")
        plt.ylabel("Aylık İyileşen Kişi Sayısı")
        plt.xlabel("Günler")
        plt.show()

    elif(menusec=="4"):
        plt.bar(g,tva,color="red")
        plt.suptitle("Son 1 aylık toplam vaka sayısı")
        plt.ylabel("Toplam Vaka Sayısı")
        plt.xlabel("Günler")
        plt.show()

    elif(menusec=="5"):
        plt.bar(g,tve,color="green")
        plt.suptitle("Son 1 aylık toplam vefat sayısı")
        plt.ylabel("Toplam Vefat Sayısı")
        plt.xlabel("Günler")
        plt.show()

    elif(menusec=="6"):
        plt.plot(g2,hva2,"b-",label="vaka sayısı")
        plt.plot(g2,hve2,"r-",label="vefat sayısı")
        plt.suptitle("12-13 Ağustos vaka ve vefat sayısı karsılastırma")
        plt.ylabel("Son 2 Günlük Veriler")
        plt.xlabel("Günler")
        plt.legend(loc="best")
        plt.show()

    elif(menusec=="7"):
        plt.bar(g3,veri13,color="yellow",edgecolor="orange",hatch="*")
        plt.suptitle("13 Ağustos verileri")
        plt.xlabel("13 Ağustos 2022")
        plt.show()
    
    else:
        print("Herhangi bir grafik seçmediniz.")
        break
    a = 0
    for i in secenek:
        a = a + 1
        print( a,".",i)
    menusec=input("Görmek istediğiniz tablonun numarasını giriniz. : ")
    os.system('CLS')
print("Uygulamamızı kullandğınız için teşekkür ederiz. :)")