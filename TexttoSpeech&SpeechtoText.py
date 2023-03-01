from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os
import pyttsx3

pencere= Tk()
pencere.title('Jeriko ile metin-ses dönüştürücü')
pencere.geometry('500x500')
pencere.resizable(0, 0)
pencere.configure(bg='white')

def konuşma(metin1):
    engine = pyttsx3.init()
    engine.say(metin1)
    engine.runAndWait()
    
def seskayıt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:    
            metin1 = r.recognize_google(audio,language="en-tr")
        except:
            pass
        return metin1
    

def metindensese():
    metindensesepencere = Toplevel(pencere)
    metindensesepencere.title('Metni konuşmaya dönüştürme')
    metindensesepencere.geometry("500x500")
    metindensesepencere.configure(bg='white')
 
    Label(metindensesepencere, text='Dinlemek istediğiniz metni giriniz.', font=("Times New Roman", 15), bg='white').place(x=50)
 
    text = Text(metindensesepencere, height=5, width=30, font=12)
    text.place(x=7, y=60)
   
    konuşmabutonu = Button(metindensesepencere, text='dinle', bg='white', command=lambda: konuşma(str(text.get(1.0, END))))
    konuşmabutonu.place(x=140, y=200)
 
def sestenmetne():
    sestenmetnepencere = Toplevel(pencere)
    sestenmetnepencere.title('Konuşmayı metne dönüştürme')
    sestenmetnepencere.geometry("500x500")
    sestenmetnepencere.configure(bg='white')
 
    Label(sestenmetnepencere, text='Metinleştirmek istediğiniz konuşmanızı dinletiniz.', font=("Times New Roman", 12), bg='white').place(x=50)
 
    text = Text(sestenmetnepencere, font=12, height=3, width=30)
    text.place(x=7, y=100)
   
    kayıtbuton = Button(sestenmetnepencere, text='kayıt', bg='white', command=lambda: text.insert(END, seskayıt()))
    kayıtbuton.place(x=140, y=50)
 
Label(pencere, text='Jeriko ile ister yazdığın metni seslendir\n' \
                'İster söylediklerini metin olarak yazdır.',
    font=('Times New Roman', 16), bg='white', wrap=True, wraplength=450).place(x=25, y=0)
 
metindensesebuton = Button(pencere, text='Metni seslendir', font=('Times New Roman', 16), bg='grey', command=metindensese)
metindensesebuton.place(x=100, y=150)
 
sestenmetnebuton = Button(pencere, text='Konuşmayı metinleştir', font=('Times New Roman', 16), bg='grey', command=sestenmetne)
sestenmetnebuton.place(x=100, y=250)
 
pencere.update()
pencere.mainloop()

