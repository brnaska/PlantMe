import io
import tkinter as tk
from tkinter import *
import urllib.request
from PIL import Image, ImageTk
from urllib.request import urlopen
import json
import sqlite3
from datetime import date, datetime

now=datetime.now()
mojaappdan=now.strftime("%d.%m.%Y.")
mojaappsat=now.strftime("%H:%M:%S")

urljson=f'https://api.tutiempo.net/json/?lan=en&apid=zwDX4azaz4X4Xqs&ll=43.51436051979722,16.444448215112512'
response=urlopen(urljson)
data_json=json.loads(response.read())
#print(data_json)

root = tk.Tk()
root.title(f'PyFloraPosuda aplikacija - Prijava')
root['bg'] = 'DarkSeaGreen'
root.geometry('600x450')

bad_pass=Label(root, text='Pogresno korisnicko ime \nili lozinka!', font=('Calibri', 20), bg='DarkSeaGreen')

def authenticate(username, password):
    with open('Korisnici.txt', 'r') as f:
        headers = f.readline().strip().split(' ')
        username_idx = headers.index('Username')
        password_idx = headers.index('Password')
        for line in f:
            values = line.strip().split(' ')
            if username == values[username_idx] and password == values[password_idx]:
                return True
    return False


def login():
    Username = userName.get()
    Password = password.get()

    if authenticate(Username, Password):
        print('Uspjesna autentifikacija!')
        open_app()
    else:
        bad_pass.grid(column=4, row=6, columnspan=3)
        bad_pass.after(3000, lambda:bad_pass.destroy())
        clearEntry()

def clearRoot(root):
    for widget in root.winfo_children():
        widget.destroy()

def clearEntry():
    password.delete(first=0, last=20)
    userName.delete(first=0, last=20)

def open_profil():
    quit

def open_detalji1():
    quit
def open_detalji2():
    quit
def open_detalji3():
    quit
def open_detalji4():
    quit

def open_biljke():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Biljke')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')
    
    ##### Frame 1 #####
    frame1 = tk.Frame(root, bg='DarkSeaGreen3', width=350, height=150)
    frame1.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

    image1 = Image.open(r'Slike/Biljke/Orhideja.jpg')
    image1 = image1.resize((150, 150), Image.ANTIALIAS)
    biljka1 = ImageTk.PhotoImage(image1)
    labelB1 = tk.Label(frame1, image=biljka1, bg='DarkSeaGreen3')
    labelB1.place(x=0, y=0)

    tegla1 = Image.open(r'Slike\Posude\Promjer12cm.jpg')
    tegla1R = tegla1.resize((70, 70), Image.ANTIALIAS)
    tegla1N = ImageTk.PhotoImage(tegla1R)
    labelT1 = tk.Label(frame1, image=tegla1N, bg='DarkSeaGreen3')
    labelT1.place(x=210,y=30)

    oBiljka1_1='1. Biljka je Orhideja, nalazi se \nu tegli:'
    oBiljka1=tk.StringVar()
    oBiljka1.set(oBiljka1_1)
    oBiljka1L=tk.Label(frame1,textvariable=oBiljka1, font=('Segoe UI',10), bg='DarkSeaGreen3', justify='left')
    oBiljka1L.place(x=155,y=0)

    oStatus1_1=f'Status: OK'
    oStatus1=tk.StringVar()
    oStatus1.set(oStatus1_1)
    oStatus1L=tk.Label(frame1,textvariable=oStatus1, font=('Segoe UI',10), bg='DarkSeaGreen3', justify='left')
    oStatus1L.place(x=155,y=110)

    detalji1Button=Button(frame1, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detalji1)
    detalji1Button.place(x=300, y=130)
     
    # ##### Frame 2 #####
    frame2 = tk.Frame(root, bg='DarkSeaGreen3', width=350, height=150)
    frame2.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

    image2 = Image.open(r'Slike\Biljke\Macuhice.jpg')
    image2 = image2.resize((150, 150), Image.ANTIALIAS)
    biljka2 = ImageTk.PhotoImage(image2)
    labelB2 = tk.Label(frame2, image=biljka2, bg='DarkSeaGreen3')
    labelB2.place(x=0, y=0)

    tegla2 = Image.open(r'Slike\Posude\Promjer9cm.jpg')
    tegla2R = tegla2.resize((70, 70), Image.ANTIALIAS)
    tegla2N = ImageTk.PhotoImage(tegla2R)
    labelT2 = tk.Label(frame2, image=tegla2N, bg='DarkSeaGreen3')
    labelT2.place(x=210,y=30)

    oBiljka2_1='2. Biljka je Macuhica, nalazi se \nu tegli:'
    oBiljka2=tk.StringVar()
    oBiljka2.set(oBiljka2_1)
    oBiljka2L=tk.Label(frame2,textvariable=oBiljka2, font=('Segoe UI',10), bg='DarkSeaGreen3', justify='left')
    oBiljka2L.place(x=155,y=0)

    oStatus2_1=f'Status: OK'
    oStatus2=tk.StringVar()
    oStatus2.set(oStatus2_1)
    oStatus2L=tk.Label(frame2,textvariable=oStatus2, font=('Segoe UI',10), bg='DarkSeaGreen3', justify='left')
    oStatus2L.place(x=155,y=110)

    detalji2Button=Button(frame2, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detalji2)
    detalji2Button.place(x=300, y=130)

    # ##### Frame 3 #####
    frame3 = tk.Frame(root, bg='DarkSeaGreen3', width=350, height=150)
    frame3.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

    image3 = Image.open(r'Slike\Biljke\Kaktus.webp')
    image3 = image3.resize((150, 150), Image.ANTIALIAS)
    biljka3 = ImageTk.PhotoImage(image3)
    labelB3 = tk.Label(frame3, image=biljka3, bg='DarkSeaGreen3')
    labelB3.place(x=0, y=0)

    tegla3 = Image.open(r'Slike\Posude\Promjer27cm.jpg')
    tegla3R = tegla3.resize((70, 70), Image.ANTIALIAS)
    tegla3N = ImageTk.PhotoImage(tegla3R)
    labelT3 = tk.Label(frame3, image=tegla3N, bg='DarkSeaGreen3')
    labelT3.place(x=210,y=30)

    oBiljka3_1='3. Biljka je Kaktus, nalazi se \nu tegli:'
    oBiljka3=tk.StringVar()
    oBiljka3.set(oBiljka3_1)
    oBiljka3L=tk.Label(frame3,textvariable=oBiljka3, font=('Segoe UI',10), bg='DarkSeaGreen3', justify='left')
    oBiljka3L.place(x=155,y=0)

    oStatus3_1=f'Status: OK'
    oStatus3=tk.StringVar()
    oStatus3.set(oStatus3_1)
    oStatus3L=tk.Label(frame3,textvariable=oStatus3, font=('Segoe UI',10), bg='DarkSeaGreen3', justify='left')
    oStatus3L.place(x=155,y=110)

    detalji3Button=Button(frame3, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detalji3)
    detalji3Button.place(x=300, y=130)

    # ##### Frame 4 #####
    frame4 = tk.Frame(root, bg='DarkSeaGreen3', width=350, height=150)
    frame4.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

    image4 = Image.open(r'Slike\Biljke\FikusBenjamin.jpg')
    image4 = image4.resize((150, 150), Image.ANTIALIAS)
    biljka4 = ImageTk.PhotoImage(image4)
    labelB4 = tk.Label(frame4, image=biljka4, bg='DarkSeaGreen3')
    labelB4.place(x=0, y=0)

    tegla4 = Image.open(r'Slike\Posude\Promjer40cm.jpg')
    tegla4R = tegla4.resize((70, 70), Image.ANTIALIAS)
    tegla4N = ImageTk.PhotoImage(tegla4R)
    labelT4 = tk.Label(frame4, image=tegla4N, bg='DarkSeaGreen3')
    labelT4.place(x=210,y=40)

    oBiljka4_1='4. Biljka je Fikus Benjamin, \n nalazi se u tegli:'
    oBiljka4=tk.StringVar()
    oBiljka4.set(oBiljka4_1)
    oBiljka4L=tk.Label(frame4,textvariable=oBiljka4, font=('Segoe UI',10), bg='DarkSeaGreen3', justify='left')
    oBiljka4L.place(x=155,y=0)

    oStatus4_1=f'Status: OK'
    oStatus4=tk.StringVar()
    oStatus4.set(oStatus4_1)
    oStatus4L=tk.Label(frame4,textvariable=oStatus4, font=('Segoe UI',10), bg='DarkSeaGreen3', justify='left')
    oStatus4L.place(x=155,y=110)

    detalji4Button=Button(frame4, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detalji4)
    detalji4Button.place(x=300, y=130)

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=70)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=100)
    
    root.mainloop()

def open_posude():
    quit

def open_app():
    clearRoot(root)
    
    root.title(f'PyFloraPosuda - Vremenska prognoza')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('950x500')

    ########  POVLACENJE PODATAKA - TUTIEMPO#####
    temperature=data_json['information']['temperature']
    wind=data_json['information']['wind']
    humidity=data_json['information']['humidity']
    pressure=data_json['information']['pressure']
    city=data_json['locality']['name']
    country=data_json['locality']['country']
    date=data_json['hour_hour']['hour1']['date']
    hour=data_json['hour_hour']['hour1']['hour_data']
    temp=data_json['hour_hour']['hour1']['temperature']
    windspeed=data_json['hour_hour']['hour1']['wind']
    humid=data_json['hour_hour']['hour1']['humidity']
    press=data_json['hour_hour']['hour1']['pressure']
    currenttext=data_json['hour_hour']['hour1']['text']
    winddirection=data_json['hour_hour']['hour1']['wind_direction']
    #icons
    iconcurrenttext=data_json['hour_hour']['hour1']['icon']
    iconwind=data_json['hour_hour']['hour1']['icon_wind']
    iconmoonphases=data_json['day1']['moon_phases_icon']

    ###### Labeli - naslov ######
    rec2=f'Grad: {city},  Drzava: {country}'
    recenica2=tk.StringVar()
    recenica2.set(rec2)
    label=tk.Label(root, textvariable=recenica2, font=('Segoe UI',16),bg='DarkSeaGreen2', justify='left')
    label.grid(column=0, row=0,padx=0,pady=0)

    rec2_1=f'Datum i sat: {mojaappdan}  {mojaappsat}'
    recenica2_1=tk.StringVar()
    recenica2_1.set(rec2_1)
    label2_1=tk.Label(root, textvariable=recenica2_1, font=('Segoe UI',16), bg='DarkSeaGreen2', justify='left')
    label2_1.grid(column=2, row=0,padx=0,pady=15)

    #### Vremenska prognoza ####
    rec3_1=f'Temperatura: {temp}{temperature}'
    recenica3_1=tk.StringVar()
    recenica3_1.set(rec3_1)
    label3_1=tk.Label(root,textvariable=recenica3_1, font=('Segoe UI',16), bg='DarkSeaGreen2', justify='left')
    label3_1.grid(column=0,columnspan=1, row=1,padx=15,pady=15)

    rec3_2=f'Vjetar: {windspeed}{wind}'
    recenica3_2=tk.StringVar()
    recenica3_2.set(rec3_2)
    label3_2=tk.Label(root,textvariable=recenica3_2, font=('Segoe UI',16), bg='DarkSeaGreen2', justify='left')
    label3_2.grid(column=0,columnspan=1, row=2,padx=15,pady=15)

    rec3_3=f'Vlaznost zraka: {humid}{humidity}'
    recenica3_3=tk.StringVar()
    recenica3_3.set(rec3_3)
    label3_3=tk.Label(root,textvariable=recenica3_3, font=('Segoe UI',16), bg='DarkSeaGreen2', justify='left')
    label3_3.grid(column=0,columnspan=1, row=3,padx=15,pady=15)

    rec3_4=f'Tlak zraka: {press}{pressure}'
    recenica3_4=tk.StringVar()
    recenica3_4.set(rec3_4)
    label3_4=tk.Label(root,textvariable=recenica3_4, font=('Segoe UI',16), bg='DarkSeaGreen2', justify='left')
    label3_4.grid(column=0,columnspan=1, row=4,padx=15,pady=15)

    rec4=f'Prognoza: {currenttext}'
    recenica4=tk.StringVar()
    recenica4.set(rec4)
    label4=tk.Label(root,textvariable=recenica4, font=('Segoe UI',16), bg='DarkSeaGreen2', justify='left')
    label4.grid(column=2, row=1, padx=0,pady=15)

    rec5=f'Vjetar {winddirection}'
    recenica5=tk.StringVar()
    recenica5.set(rec5)
    label5=tk.Label(root,textvariable=recenica5, font=('Segoe UI',16), bg='DarkSeaGreen2', justify='left')
    label5.grid(column=2, row=2, padx=0,pady=15)

    rec6=f'Mjeseceve mijene'
    recenica6=tk.StringVar()
    recenica6.set(rec6)
    label6=tk.Label(root,textvariable=recenica6, font=('Segoe UI',16), bg='DarkSeaGreen2', justify='left')
    label6.grid(column=2, row=3, padx=0,pady=15)

    ######## IKONE - Prognoza ########
    size=90
    urlimgforecast=f'https://v5i.tutiempo.net/wi/02/{size}/{iconcurrenttext}.png'
    with urllib.request.urlopen(urlimgforecast) as connection:
        raw_data=connection.read()
    im=Image.open(io.BytesIO(raw_data))
    im = im.resize((70,70))
    imageforecast=ImageTk.PhotoImage(im)

    urlimgwind=f'https://v5i.tutiempo.net/wd/big/black/{iconwind}.png'
    with urllib.request.urlopen(urlimgwind) as connection:
        raw_data=connection.read()
    im=Image.open(io.BytesIO(raw_data))
    im = im.resize((70,70))
    imagewind=ImageTk.PhotoImage(im)

    urlimgmoon=f'https://v5i.tutiempo.net/wmi/02/{iconmoonphases}.png'
    with urllib.request.urlopen(urlimgmoon) as connection:
        raw_data=connection.read()
    im=Image.open(io.BytesIO(raw_data))
    im = im.resize((70,70))
    imagemoon=ImageTk.PhotoImage(im)

    imgforecast=tk.Label(root, image=imageforecast, bg='DarkSeaGreen2')
    imgforecast.grid(column=4, row=1,padx=30,pady=15)
    imgwind=tk.Label(root, image=imagewind, bg='DarkSeaGreen2')
    imgwind.grid(column=4, row=2,padx=30,pady=15)
    imgmoon=tk.Label(root, image=imagemoon, bg='DarkSeaGreen2')
    imgmoon.grid(column=4, row=3,padx=30,pady=15)

    imgTemp=Image.open("Slike\Vremenska_prognoza\Temperatura.jpg")
    imgTempR=imgTemp.resize((70,70), Image.ANTIALIAS)
    imgTempN= ImageTk.PhotoImage(imgTempR)
    label=Label(root, image=imgTempN)
    label.grid(column=1, row=1)

    imgVjetar=Image.open("Slike\Vremenska_prognoza\Vjetar.jpg")
    imgVjetarR=imgVjetar.resize((70,70), Image.ANTIALIAS)
    imgVjetarN= ImageTk.PhotoImage(imgVjetarR)
    label=Label(root, image=imgVjetarN)
    label.grid(column=1, row=2)

    imgVlaznost=Image.open("Slike\Vremenska_prognoza\Vlaznost.jpg")
    imgVlaznostR=imgVlaznost.resize((70,70), Image.ANTIALIAS)
    imgVlaznostN= ImageTk.PhotoImage(imgVlaznostR)
    label=Label(root, image=imgVlaznostN)
    label.grid(column=1, row=3)

    imgTlak=Image.open("Slike\Vremenska_prognoza\Tlak.jpg")
    imgTlakR=imgTlak.resize((70,70), Image.ANTIALIAS)
    imgTlakN= ImageTk.PhotoImage(imgTlakR)
    label=Label(root, image=imgTlakN)
    label.grid(column=1, row=4)
    
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=800, y=10)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=800, y=40)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=800, y=70)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=800, y=100)

    root.mainloop()

######### PRIJAVA ######
prijava=tk.Label(root,text="Prijava", font=('Calibri', 20), bg='DarkSeaGreen')
prijava.grid(column=5, row=0, columnspan=2, padx=40)
korisnickoIme=tk.Label(root,text="Korisnicko ime", font=('Calibri', 15), bg='DarkSeaGreen')
korisnickoIme.grid(column=5, row=1, columnspan=3, padx=40)
userName= Entry(root,show="",width=20)
userName.grid(column=5, row=2, columnspan=2, padx=40)
lozinka=tk.Label(root,text="Lozinka", font=('Calibri', 15), bg='DarkSeaGreen')
lozinka.grid(column=5, row=3, columnspan=2, padx=40)
password= Entry(root,show="*",width=20)
password.grid(column=5, row=4, columnspan=2, padx=40)
loginButton=Button(root, text="Prijavi me",width=10, font=('Helvetica bold',13),command=login).grid(column=5, row=5, padx=40)
cancelButton=Button(root, text="Izlaz",width=10, font=('Helvetica bold',13),command=quit).grid(column=6, row=5, padx=40)

img1=Image.open("Slike/Login/Slika2_login.jpg")
img1R=img1.resize((200,200), Image.ANTIALIAS)
img1New= ImageTk.PhotoImage(img1R)
label=Label(root, image=img1New)
label.grid(column=2, row=1, columnspan=2, rowspan=3)

root.mainloop()
