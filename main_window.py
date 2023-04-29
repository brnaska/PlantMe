import io
import tkinter as tk
from tkinter import *
import urllib.request
from PIL import Image, ImageTk
from urllib.request import urlopen
import json
import sqlite3
from datetime import date, datetime
import random

now=datetime.now()
mojaappdan=now.strftime("%d.%m.%Y.")
mojaappsat=now.strftime("%H:%M:%S")

urljson=f'https://api.tutiempo.net/json/?lan=en&apid=zwDX4azaz4X4Xqs&ll=43.51436051979722,16.444448215112512'
response=urlopen(urljson)
data_json=json.loads(response.read())

def open_app(root):
    import main
    main.clearRoot(root)
    root.title(f'PyFloraPosuda - Vremenska prognoza')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('950x500')

    ########  POVLACENJE PODATAKA - TUTIEMPO  #####
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

    ##############    Vremenska prognoza    #############
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
    
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=main.open_profil).place(x=800, y=10)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=main.open_biljke).place(x=800, y=40)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=main.open_posude).place(x=800, y=70)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=800, y=100)

    root.mainloop()