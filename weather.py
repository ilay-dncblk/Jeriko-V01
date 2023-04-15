from os import link
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

print("Merhaba ben Jeriko. Şehrinin hava durumunu göstermek ve yorumlamak için buradayım. Hoş geldiniz.\n")

def yorum(bölge):
    if(bölge=="Açık"):
        print("Gökyüzü çok güzel.")
    elif(bölge=="Karlı"):
        print("Hasta olmamak için sıkı giyinmeniz gereken bir gün. Eldiven, atkı, bere takınabilirsiniz.")
    elif(bölge=="Rüzgarlı"):
        print("Rüzgar sonucu uçacak kıyafet ve aksesuarlardan kaçınabilirsiniz.")
    elif(bölge=="Az Bulutlu"):
        print("Güneş, birkaç bulut... Günün tadını çıkarabilirsiniz.")
    elif(bölge=="Bulutlu"):
        print("Üzerinize ince bir hırka almanızda fayda var.")
    elif(bölge=="Çok Bulutlu"):
        print("Yağmur yağma ihtimaline karşın şemsiyenizi yanınıza alabilirsiniz.")
    elif(bölge=="Sisli"):
        print("Görüşünüzü zorlayacak bir sis ile karşı karşıya kalabilirsiniz. Önemli bir işiniz yoksa dışarı çıkmak için uygun bir gün değil gibi gözüküyor.")
    elif(bölge=="Güneşli"):
        print("Başınıza güneş geçmemesi için yanınızda şemsiye ya da şapka bulundurun.")
    elif(bölge=="Kapalı"):
        print("Yağmur yağabilir veya rüzgar çıkabilir.")


def engine(link):
    driver = webdriver.Chrome()
    driver.get(link)
    
    time.sleep(2)
    ilSicaklik = driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/section/div[5]/div[1]/div[1]").text
    ilDurum = driver.find_element(By.CLASS_NAME, value="anlik-sicaklik-havadurumu-ikonismi").text
    print(link.partition("=")[2] + " ili için hava sıcaklığı: " + ilSicaklik + " derece ve hava " + ilDurum)
    yorum(ilDurum)
        
def engine2(link):
    driver = webdriver.Chrome()
    driver.get(link)
    
    time.sleep(2)
    ilceSicaklik = driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/section/div[5]/div[1]/div[1]").text
    ilceDurum = driver.find_element(By.CLASS_NAME, value="anlik-sicaklik-havadurumu-ikonismi").text
    print(link.partition("e=")[2] + " ilçe için hava sıcaklığı: " + ilceSicaklik + " derece ve hava " + ilceDurum)
    yorum(ilceDurum)



print("Bilgiler anlık olarak Meteroloji Genel Müdürlüğünden Alınmaktadır...") 

given_il =input("\nHava durumunu görmek istediğiniz ili giriniz: ")
given_ilce =input("\nHava durumunu görmek istediğiniz ilçeyi giriniz: (ilçe girmek istemiyorsanız enter tuşuna basınız.)")
if(given_ilce==""):
    tempLink=("https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=%s" %(given_il))
    engine(tempLink)
else:
    tempLink2 = ("https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=%s&ilce=%s" %(given_il,given_ilce))
    engine2(tempLink2)