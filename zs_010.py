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
print(data_json)

root = tk.Tk()
root.title(f'PyFloraPosuda aplikacija - Prijava')
root['bg'] = 'DarkSeaGreen'
root.geometry('600x450')

############################### PRIJAVA --> AUTENTIFIKACIJA ##########################
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
bad_pass=Label(root, text='Pogresno korisnicko ime \nili lozinka!', font=('Calibri', 20), bg='DarkSeaGreen')
def login():
    Username = userName.get()
    Password = password.get()
    if authenticate(Username, Password):
        print('Uspjesna autentifikacija!')
        open_app()
    else:
        bad_pass.place(x=250, y=280)
        bad_pass.after(3000, lambda:bad_pass.destroy())
        clearEntry()

################################# CISCENJE EKRANA --> APLIKACIJA  ##########################
def clearRoot(root):
    for widget in root.winfo_children():
        widget.destroy()

################################## CISCENJE UNOSA --> PRIJAVA ###############################
def clearEntry():
    password.delete(first=0, last=20)
    userName.delete(first=0, last=20)

################################### BUTTON --> MOJ PROFIL ####################################
def open_profil():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Profil')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    profil1 = Image.open(r'Slike\Slika_profila\Profil1.jpg')
    profil1R = profil1.resize((200, 200), Image.ANTIALIAS)
    profil1N = ImageTk.PhotoImage(profil1R)
    profilT1 = tk.Label(root, image=profil1N, bg='DarkSeaGreen2')
    profilT1.place(x=10,y=30)

    ime1_1='Ime'
    ime1=tk.StringVar()
    ime1.set(ime1_1)
    ime1L=tk.Label(root,textvariable=ime1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    ime1L.place(x=300,y=20)

    prezime1_1='Prezime'
    prezime1=tk.StringVar()
    prezime1.set(prezime1_1)
    prezime1L=tk.Label(root,textvariable=prezime1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    prezime1L.place(x=300,y=60)

    korisnickoime1_1='Korisnicko ime'
    korisnickoime1=tk.StringVar()
    korisnickoime1.set(korisnickoime1_1)
    korisnickoime1L=tk.Label(root,textvariable=korisnickoime1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    korisnickoime1L.place(x=300,y=100)

    lozinka1_1='Lozinka'
    lozinka1=tk.StringVar()
    lozinka1.set(lozinka1_1)
    lozinka1L=tk.Label(root,textvariable=lozinka1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    lozinka1L.place(x=300,y=140)

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=40)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=70)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=100)

    root.mainloop()

#################################### DETALJI --> BILJKE ####################################
def open_detalji1():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Biljke')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    biljka1 = Image.open(r'Slike/Biljke/Orhideja.jpg')
    biljka1R = biljka1.resize((250, 250), Image.ANTIALIAS)
    biljka1N = ImageTk.PhotoImage(biljka1R)
    labelB1 = tk.Label(root, image=biljka1N, bg='DarkSeaGreen3')
    labelB1.place(x=400,y=70)

    oBiljka1_1='1. Orhideja - Odrazavanje'
    oBiljka1=tk.StringVar()
    oBiljka1.set(oBiljka1_1)
    oBiljka1L=tk.Label(root,textvariable=oBiljka1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oBiljka1L.place(x=80,y=40)

    oTemperatura1_1='Temperatura: 23-29 °C'
    oTemperatura1=tk.StringVar()
    oTemperatura1.set(oTemperatura1_1)
    oTemperatura1L=tk.Label(root,textvariable=oTemperatura1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oTemperatura1L.place(x=100,y=90)

    oVlaznost1_1='Vlaznost: 40-70 %'
    oVlaznost1=tk.StringVar()
    oVlaznost1.set(oVlaznost1_1)
    oVlaznost1L=tk.Label(root,textvariable=oVlaznost1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oVlaznost1L.place(x=100,y=140)

    oSvjetlost1_1='Svjetlost: 4500-6000 K'
    oSvjetlost1=tk.StringVar()
    oSvjetlost1.set(oSvjetlost1_1)
    oSvjetlost1L=tk.Label(root,textvariable=oSvjetlost1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSvjetlost1L.place(x=100,y=190)

    oHrana1_1='Hrana: 70-100 %'
    oHrana1=tk.StringVar()
    oHrana1.set(oHrana1_1)
    oHrana1L=tk.Label(root,textvariable=oHrana1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oHrana1L.place(x=100,y=240)

    oPolozaj1_1='Polozaj: Prozor kuhinje'
    oPolozaj1=tk.StringVar()
    oPolozaj1.set(oPolozaj1_1)
    oPolozaj1L=tk.Label(root,textvariable=oPolozaj1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oPolozaj1L.place(x=100,y=290)
    
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=130)

    root.mainloop()

def open_detalji2():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Biljke')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    biljka2 = Image.open(r'Slike\Biljke\Macuhice.jpg')
    biljka2R = biljka2.resize((250, 250), Image.ANTIALIAS)
    biljka2N = ImageTk.PhotoImage(biljka2R)
    labelB2 = tk.Label(root, image=biljka2N, bg='DarkSeaGreen3')
    labelB2.place(x=400,y=70)

    oBiljka2_1='2. Macuhice - Odrazavanje'
    oBiljka2=tk.StringVar()
    oBiljka2.set(oBiljka2_1)
    oBiljka2L=tk.Label(root,textvariable=oBiljka2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oBiljka2L.place(x=80,y=40)

    oTemperatura2_1='Temperatura: 15-21 °C'
    oTemperatura2=tk.StringVar()
    oTemperatura2.set(oTemperatura2_1)
    oTemperatura2L=tk.Label(root,textvariable=oTemperatura2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oTemperatura2L.place(x=100,y=90)

    oVlaznost2_1='Vlaznost: 40-60 %'
    oVlaznost2=tk.StringVar()
    oVlaznost2.set(oVlaznost2_1)
    oVlaznost2L=tk.Label(root,textvariable=oVlaznost2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oVlaznost2L.place(x=100,y=140)

    oSvjetlost2_1='Svjetlost: 4500-6500 K'
    oSvjetlost2=tk.StringVar()
    oSvjetlost2.set(oSvjetlost2_1)
    oSvjetlost2L=tk.Label(root,textvariable=oSvjetlost2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSvjetlost2L.place(x=100,y=190)

    oHrana2_1='Hrana: 70-100 %'
    oHrana2=tk.StringVar()
    oHrana2.set(oHrana2_1)
    oHrana2L=tk.Label(root,textvariable=oHrana2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oHrana2L.place(x=100,y=240)

    oPolozaj2_1='Polozaj: Prozor WC-a'
    oPolozaj2=tk.StringVar()
    oPolozaj2.set(oPolozaj2_1)
    oPolozaj2L=tk.Label(root,textvariable=oPolozaj2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oPolozaj2L.place(x=100,y=290)
    
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=130)
   
    root.mainloop()

def open_detalji3():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Biljke')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    biljka3 = Image.open(r'Slike\Biljke\Kaktus.webp')
    biljka3R = biljka3.resize((250, 250), Image.ANTIALIAS)
    biljka3N = ImageTk.PhotoImage(biljka3R)
    labelB3 = tk.Label(root, image=biljka3N, bg='DarkSeaGreen3')
    labelB3.place(x=400,y=70)

    oBiljka3_1='3. Kaktus - Odrazavanje'
    oBiljka3=tk.StringVar()
    oBiljka3.set(oBiljka3_1)
    oBiljka3L=tk.Label(root,textvariable=oBiljka3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oBiljka3L.place(x=80,y=40)

    oTemperatura3_1='Temperatura: 22-32 °C'
    oTemperatura3=tk.StringVar()
    oTemperatura3.set(oTemperatura3_1)
    oTemperatura3L=tk.Label(root,textvariable=oTemperatura3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oTemperatura3L.place(x=100,y=90)

    oVlaznost3_1='Vlaznost: 20-40 %'
    oVlaznost3=tk.StringVar()
    oVlaznost3.set(oVlaznost3_1)
    oVlaznost3L=tk.Label(root,textvariable=oVlaznost3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oVlaznost3L.place(x=100,y=140)

    oSvjetlost3_1='Svjetlost: 5000-6500 K'
    oSvjetlost3=tk.StringVar()
    oSvjetlost3.set(oSvjetlost3_1)
    oSvjetlost3L=tk.Label(root,textvariable=oSvjetlost3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSvjetlost3L.place(x=100,y=190)

    oHrana3_1='Hrana: 70-100 %'
    oHrana3=tk.StringVar()
    oHrana3.set(oHrana3_1)
    oHrana3L=tk.Label(root,textvariable=oHrana3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oHrana3L.place(x=100,y=240)

    oPolozaj3_1='Polozaj: Staklena balkonska\n\tvrata'
    oPolozaj3=tk.StringVar()
    oPolozaj3.set(oPolozaj3_1)
    oPolozaj3L=tk.Label(root,textvariable=oPolozaj3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oPolozaj3L.place(x=100,y=290)
    
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=130)
   
    root.mainloop()

def open_detalji4():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Biljke')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    biljka4 = Image.open(r'Slike\Biljke\FikusBenjamin.jpg')
    biljka4R = biljka4.resize((250, 250), Image.ANTIALIAS)
    biljka4N = ImageTk.PhotoImage(biljka4R)
    labelB4 = tk.Label(root, image=biljka4N, bg='DarkSeaGreen3')
    labelB4.place(x=400,y=70)

    oBiljka4_1='4. Fikus Benjamin - Odrazavanje'
    oBiljka4=tk.StringVar()
    oBiljka4.set(oBiljka4_1)
    oBiljka4L=tk.Label(root,textvariable=oBiljka4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oBiljka4L.place(x=80,y=40)

    oTemperatura4_1='Temperatura: 20-28 °C'
    oTemperatura4=tk.StringVar()
    oTemperatura4.set(oTemperatura4_1)
    oTemperatura4L=tk.Label(root,textvariable=oTemperatura4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oTemperatura4L.place(x=100,y=90)

    oVlaznost4_1='Vlaznost: 40-75 %'
    oVlaznost4=tk.StringVar()
    oVlaznost4.set(oVlaznost4_1)
    oVlaznost4L=tk.Label(root,textvariable=oVlaznost4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oVlaznost4L.place(x=100,y=140)

    oSvjetlost4_1='Svjetlost: 4000-5500 K'
    oSvjetlost4=tk.StringVar()
    oSvjetlost4.set(oSvjetlost4_1)
    oSvjetlost4L=tk.Label(root,textvariable=oSvjetlost4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSvjetlost4L.place(x=100,y=190)

    oHrana4_1='Hrana: 70-100 %'
    oHrana4=tk.StringVar()
    oHrana4.set(oHrana4_1)
    oHrana4L=tk.Label(root,textvariable=oHrana4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oHrana4L.place(x=100,y=240)

    oPolozaj4_1='Polozaj: Kut dnevnog\n\tboravka'
    oPolozaj4=tk.StringVar()
    oPolozaj4.set(oPolozaj4_1)
    oPolozaj4L=tk.Label(root,textvariable=oPolozaj4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oPolozaj4L.place(x=100,y=290)
    
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=130)
   
    root.mainloop()

######################################## DETALJI --> POSUDE #############################
def open_detaljiT1():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Posude')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    image1 = Image.open(r'Slike\Posude\Promjer12cm.jpg')
    image1 = image1.resize((150, 150), Image.ANTIALIAS)
    tegla1 = ImageTk.PhotoImage(image1)
    labelT1 = tk.Label(root, image=tegla1, bg='DarkSeaGreen2')
    labelT1.place(x=0, y=0)

    oTegla1_1='1. Bijela tegla za cvijece promjera 12 cm'
    oTegla1=tk.StringVar()
    oTegla1.set(oTegla1_1)
    oTegla1L=tk.Label(root,textvariable=oTegla1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oTegla1L.place(x=180,y=0)

    vlaga1 = random.randrange(30,70)
    oSenzor1_1=f'Senzor Vlage:\t{vlaga1} %'
    oSenzor1=tk.StringVar()
    oSenzor1.set(oSenzor1_1)
    oSenzorL=tk.Label(root,textvariable=oSenzor1, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzorL.place(x=185,y=35)

    svjetlost1 = random.randrange(2500,6500)
    oSenzor2_1=f'Senzor Svjetla:\t{svjetlost1} K'
    oSenzor2=tk.StringVar()
    oSenzor2.set(oSenzor2_1)
    oSenzor2L=tk.Label(root,textvariable=oSenzor2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor2L.place(x=185,y=70)

    hrana1 = random.randrange(0,100)
    oSenzor3_1=f'Senzor Hrane:\t{hrana1} %'
    oSenzor3=tk.StringVar()
    oSenzor3.set(oSenzor3_1)
    oSenzor3L=tk.Label(root,textvariable=oSenzor3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor3L.place(x=185,y=105)

    temperatura1 = random.randrange(15,30)
    oSenzor4_1=f'Senzor temperature: {temperatura1} °C'
    oSenzor4=tk.StringVar()
    oSenzor4.set(oSenzor4_1)
    oSenzor4L=tk.Label(root,textvariable=oSenzor4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor4L.place(x=185,y=140)

    biljka1 = Image.open(r'Slike/Biljke/Orhideja.jpg')
    biljka1R = biljka1.resize((90, 90), Image.ANTIALIAS)
    biljka1N = ImageTk.PhotoImage(biljka1R)
    labelB1 = tk.Label(root, image=biljka1N, bg='DarkSeaGreen3')
    labelB1.place(x=760,y=170)

    create_table_query= '''CREATE TABLE IF NOT EXISTS Senzori_Posude_1(
                                id INTEGER PRIMARY KEY,
                                dan TEXT NOT NULL,
                                sat TEXT NOT NULL,
                                vlaga1 TEXT NOT NULL,
                                svjetlost1 TEXT NOT NULL,
                                hrana1 TEXT NOT NULL,
                                temperatura1 TEXT NOT NULL);'''

    database_name='Povijest senzora_Posuda 1.db'

    try:
        sqliteConnection=sqlite3.connect(database_name)
        cursor=sqliteConnection.cursor()
        print(f'SQLite baza {database_name} je kreirana i spojena')
        cursor.execute(create_table_query)
        sqliteConnection.commit()       #commit primjenjuje nas upit
        print('Tabela vrijednosti senzora dodana u bazu')
        cursor.close()
        print('CURSOR otpusten')
    except sqlite3.Error as error:
        print('Doslo je do pogreske prilikom spajanja na bazu: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite verzija je zatvorena.')

    insert_into_table_query='''INSERT INTO Senzori_Posude_1 ( dan, sat, vlaga1, svjetlost1, hrana1, temperatura1)    
                                VALUES (?,?,?,?,?,?)'''
    
    try:
        sqliteConnection=sqlite3.connect(database_name)
        cursor=sqliteConnection.cursor()
        print(f'SQLite baza {database_name} je kreirana i spojena')
        cursor.execute(insert_into_table_query, (mojaappdan, mojaappsat, vlaga1, svjetlost1, hrana1, temperatura1))
        sqliteConnection.commit()
        cursor.close()
        print('CURSOR otpusten')
    except sqlite3.Error as error:
        print('Doslo je do pogreske prilikom spajanja na bazu: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite verzija je zatvorena.')

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=130)

    root.mainloop()

def open_detaljiT2():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Posude')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    image2 = Image.open(r'Slike\Posude\Promjer9cm.jpg')
    image2 = image2.resize((150, 150), Image.ANTIALIAS)
    tegla2 = ImageTk.PhotoImage(image2)
    labelT2 = tk.Label(root, image=tegla2, bg='DarkSeaGreen2')
    labelT2.place(x=0, y=0)

    oTegla2_1='2. Smeda tegla za cvijece promjera 9 cm'
    oTegla2=tk.StringVar()
    oTegla2.set(oTegla2_1)
    oTegla2L=tk.Label(root,textvariable=oTegla2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oTegla2L.place(x=180,y=0)

    vlaga2 = random.randrange(30,70)
    oSenzor1_2_1=f'Senzor Vlage:\t{vlaga2} %'
    oSenzor1_2=tk.StringVar()
    oSenzor1_2.set(oSenzor1_2_1)
    oSenzor1_2L=tk.Label(root,textvariable=oSenzor1_2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor1_2L.place(x=185,y=35)

    svjetlost2 = random.randrange(2500,6500)
    oSenzor2_2_1=f'Senzor Svjetla:\t{svjetlost2} K'
    oSenzor2_2=tk.StringVar()
    oSenzor2_2.set(oSenzor2_2_1)
    oSenzor2_2L=tk.Label(root,textvariable=oSenzor2_2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor2_2L.place(x=185,y=70)

    hrana2 = random.randrange(0,100)
    oSenzor3_2_1=f'Senzor Hrane:\t{hrana2} %'
    oSenzor3_2=tk.StringVar()
    oSenzor3_2.set(oSenzor3_2_1)
    oSenzor3_2L=tk.Label(root,textvariable=oSenzor3_2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor3_2L.place(x=185,y=105)

    temperatura2= random.randrange(15,30)
    oSenzor4_2_1=f'Senzor temperature: {temperatura2} °C'
    oSenzor4_2=tk.StringVar()
    oSenzor4_2.set(oSenzor4_2_1)
    oSenzor4_2L=tk.Label(root,textvariable=oSenzor4_2, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor4_2L.place(x=185,y=140)

    biljka2 = Image.open(r'Slike\Biljke\Macuhice.jpg')
    biljka2R = biljka2.resize((90, 90), Image.ANTIALIAS)
    biljka2N = ImageTk.PhotoImage(biljka2R)
    labelB2 = tk.Label(root, image=biljka2N, bg='DarkSeaGreen3')
    labelB2.place(x=760,y=170)

    create_table_query= '''CREATE TABLE IF NOT EXISTS Senzori_Posude_2(
                                id INTEGER PRIMARY KEY,
                                dan TEXT NOT NULL,
                                sat TEXT NOT NULL,
                                vlaga2 TEXT NOT NULL,
                                svjetlost2 TEXT NOT NULL,
                                hrana2 TEXT NOT NULL,
                                temperatura2 TEXT NOT NULL);'''

    database_name='Povijest senzora_Posuda 2.db'

    try:
        sqliteConnection=sqlite3.connect(database_name)
        cursor=sqliteConnection.cursor()
        print(f'SQLite baza {database_name} je kreirana i spojena')
        cursor.execute(create_table_query)
        sqliteConnection.commit()       #commit primjenjuje nas upit
        print('Tabela vrijednosti senzora dodana u bazu')
        cursor.close()
        print('CURSOR otpusten')
    except sqlite3.Error as error:
        print('Doslo je do pogreske prilikom spajanja na bazu: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite verzija je zatvorena.')


    insert_into_table_query='''INSERT INTO Senzori_Posude_2 ( dan, sat, vlaga2, svjetlost2, hrana2, temperatura2)    
                                VALUES (?,?,?,?,?,?)'''
    
    try:
        sqliteConnection=sqlite3.connect(database_name)
        cursor=sqliteConnection.cursor()
        print(f'SQLite baza {database_name} je kreirana i spojena')
        cursor.execute(insert_into_table_query, (mojaappdan, mojaappsat, vlaga2, svjetlost2, hrana2, temperatura2))
        sqliteConnection.commit()
        cursor.close()
        print('CURSOR otpusten')
    except sqlite3.Error as error:
        print('Doslo je do pogreske prilikom spajanja na bazu: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite verzija je zatvorena.')

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=130)

    root.mainloop()

def open_detaljiT3():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Posude')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    image3 = Image.open(r'Slike\Posude\Promjer27cm.jpg')
    image3 = image3.resize((150, 150), Image.ANTIALIAS)
    tegla3 = ImageTk.PhotoImage(image3)
    labelT3 = tk.Label(root, image=tegla3, bg='DarkSeaGreen2')
    labelT3.place(x=0, y=0)

    oTegla3_1='3. Bijela tegla za cvijece promjera 27 cm'
    oTegla3=tk.StringVar()
    oTegla3.set(oTegla3_1)
    oTegla3L=tk.Label(root,textvariable=oTegla3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oTegla3L.place(x=180,y=0)

    vlaga3 = random.randrange(30,70)
    oSenzor1_3_1=f'Senzor Vlage:\t{vlaga3} %'
    oSenzor1_3=tk.StringVar()
    oSenzor1_3.set(oSenzor1_3_1)
    oSenzor1_3L=tk.Label(root,textvariable=oSenzor1_3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor1_3L.place(x=185,y=35)

    svjetlost3 = random.randrange(2500,6500)
    oSenzor2_3_1=f'Senzor Svjetla:\t{svjetlost3} K'
    oSenzor2_3=tk.StringVar()
    oSenzor2_3.set(oSenzor2_3_1)
    oSenzor2_3L=tk.Label(root,textvariable=oSenzor2_3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor2_3L.place(x=185,y=70)

    hrana3 = random.randrange(0,100)
    oSenzor3_3_1=f'Senzor Hrane:\t{hrana3} %'
    oSenzor3_3=tk.StringVar()
    oSenzor3_3.set(oSenzor3_3_1)
    oSenzor3_3L=tk.Label(root,textvariable=oSenzor3_3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor3_3L.place(x=185,y=105)

    temperatura3= random.randrange(15,30)
    oSenzor4_3_1=f'Senzor temperature: {temperatura3} °C'
    oSenzor4_3=tk.StringVar()
    oSenzor4_3.set(oSenzor4_3_1)
    oSenzor4_3L=tk.Label(root,textvariable=oSenzor4_3, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor4_3L.place(x=185,y=140)

    biljka3 = Image.open(r'Slike\Biljke\Kaktus.webp')
    biljka3R = biljka3.resize((90, 90), Image.ANTIALIAS)
    biljka3N = ImageTk.PhotoImage(biljka3R)
    labelB3 = tk.Label(root, image=biljka3N, bg='DarkSeaGreen3')
    labelB3.place(x=760,y=170)

    create_table_query= '''CREATE TABLE IF NOT EXISTS Senzori_Posude_3 (
                                id INTEGER PRIMARY KEY,
                                dan TEXT NOT NULL,
                                sat TEXT NOT NULL,
                                vlaga3 TEXT NOT NULL,
                                svjetlost3 TEXT NOT NULL,
                                hrana3 TEXT NOT NULL,
                                temperatura3 TEXT NOT NULL);'''

    database_name='Povijest senzora_Posuda 3.db'

    try:
        sqliteConnection=sqlite3.connect(database_name)
        cursor=sqliteConnection.cursor()
        print(f'SQLite baza {database_name} je kreirana i spojena')
        cursor.execute(create_table_query)
        sqliteConnection.commit()       #commit primjenjuje nas upit
        print('Tabela vrijednosti senzora dodana u bazu')
        cursor.close()
        print('CURSOR otpusten')
    except sqlite3.Error as error:
        print('Doslo je do pogreske prilikom spajanja na bazu: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite verzija je zatvorena.')

    insert_into_table_query='''INSERT INTO Senzori_Posude_3 ( dan, sat, vlaga3, svjetlost3, hrana3, temperatura3)    
                                VALUES (?,?,?,?,?,?)'''
    
    try:
        sqliteConnection=sqlite3.connect(database_name)
        cursor=sqliteConnection.cursor()
        print(f'SQLite baza {database_name} je kreirana i spojena')
        cursor.execute(insert_into_table_query, (mojaappdan, mojaappsat, vlaga3, svjetlost3, hrana3, temperatura3))
        sqliteConnection.commit()
        cursor.close()
        print('CURSOR otpusten')
    except sqlite3.Error as error:
        print('Doslo je do pogreske prilikom spajanja na bazu: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite verzija je zatvorena.')

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=130)

    root.mainloop()

def open_detaljiT4():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Posude')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    image4 = Image.open(r'Slike\Posude\Promjer40cm.jpg')
    image4 = image4.resize((150, 150), Image.ANTIALIAS)
    tegla4 = ImageTk.PhotoImage(image4)
    labelT4 = tk.Label(root, image=tegla4, bg='DarkSeaGreen2')
    labelT4.place(x=0, y=0)

    oTegla4_1='4. Crna tegla za cvijece promjera 40 cm'
    oTegla4=tk.StringVar()
    oTegla4.set(oTegla4_1)
    oTegla4L=tk.Label(root,textvariable=oTegla4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oTegla4L.place(x=180,y=0)

    vlaga4 = random.randrange(30,70)
    oSenzor1_4_1=f'Senzor Vlage:\t{vlaga4} %'
    oSenzor1_4=tk.StringVar()
    oSenzor1_4.set(oSenzor1_4_1)
    oSenzor1_4L=tk.Label(root,textvariable=oSenzor1_4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor1_4L.place(x=185,y=35)

    svjetlost4 = random.randrange(2500,6500)
    oSenzor2_4_1=f'Senzor Svjetla:\t{svjetlost4} K'
    oSenzor2_4=tk.StringVar()
    oSenzor2_4.set(oSenzor2_4_1)
    oSenzor2_4L=tk.Label(root,textvariable=oSenzor2_4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor2_4L.place(x=185,y=70)

    hrana4 = random.randrange(0,100)
    oSenzor3_4_1=f'Senzor Hrane:\t{hrana4} %'
    oSenzor3_4=tk.StringVar()
    oSenzor3_4.set(oSenzor3_4_1)
    oSenzor3_4L=tk.Label(root,textvariable=oSenzor3_4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor3_4L.place(x=185,y=105)

    temperatura4= random.randrange(15,30)
    oSenzor4_4_1=f'Senzor temperature: {temperatura4} °C'
    oSenzor4_4=tk.StringVar()
    oSenzor4_4.set(oSenzor4_4_1)
    oSenzor4_4L=tk.Label(root,textvariable=oSenzor4_4, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
    oSenzor4_4L.place(x=185,y=140)

    biljka4 = Image.open(r'Slike\Biljke\FikusBenjamin.jpg')
    biljka4R = biljka4.resize((90, 90), Image.ANTIALIAS)
    biljka4N = ImageTk.PhotoImage(biljka4R)
    labelB4 = tk.Label(root, image=biljka4N, bg='DarkSeaGreen3')
    labelB4.place(x=760,y=170)

    create_table_query= '''CREATE TABLE IF NOT EXISTS Senzori_Posude_4(
                                id INTEGER PRIMARY KEY,
                                dan TEXT NOT NULL,
                                sat TEXT NOT NULL,
                                vlaga4 TEXT NOT NULL,
                                svjetlost4 TEXT NOT NULL,
                                hrana4 TEXT NOT NULL,
                                temperatura4 TEXT NOT NULL);'''

    database_name='Povijest senzora_Posuda 4.db'

    try:
        sqliteConnection=sqlite3.connect(database_name)
        cursor=sqliteConnection.cursor()
        print(f'SQLite baza {database_name} je kreirana i spojena')
        cursor.execute(create_table_query)
        sqliteConnection.commit()       #commit primjenjuje nas upit
        print('Tabela vrijednosti senzora dodana u bazu')
        cursor.close()
        print('CURSOR otpusten')
    except sqlite3.Error as error:
        print('Doslo je do pogreske prilikom spajanja na bazu: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite verzija je zatvorena.')

    insert_into_table_query='''INSERT INTO Senzori_Posude_4 ( dan, sat, vlaga4, svjetlost4, hrana4, temperatura4)    
                                VALUES (?,?,?,?,?,?)'''
    
    try:
        sqliteConnection=sqlite3.connect(database_name)
        cursor=sqliteConnection.cursor()
        print(f'SQLite baza {database_name} je kreirana i spojena')
        cursor.execute(insert_into_table_query, (mojaappdan, mojaappsat, vlaga4, svjetlost4, hrana4, temperatura4))
        sqliteConnection.commit()
        cursor.close()
        print('CURSOR otpusten')
    except sqlite3.Error as error:
        print('Doslo je do pogreske prilikom spajanja na bazu: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite verzija je zatvorena.')

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=130)

    root.mainloop()

#########################################  BUTTON BILJKE   ##################################
def open_biljke():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Biljke')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')
    
    ############ Frame 1 ############
    frame1 = tk.Frame(root, bg='DarkSeaGreen2', width=350, height=150)
    frame1.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

    image1 = Image.open(r'Slike/Biljke/Orhideja.jpg')
    image1 = image1.resize((150, 150), Image.ANTIALIAS)
    biljka1 = ImageTk.PhotoImage(image1)
    labelB1 = tk.Label(frame1, image=biljka1, bg='DarkSeaGreen2')
    labelB1.place(x=0, y=0)

    tegla1 = Image.open(r'Slike\Posude\Promjer12cm.jpg')
    tegla1R = tegla1.resize((70, 70), Image.ANTIALIAS)
    tegla1N = ImageTk.PhotoImage(tegla1R)
    labelT1 = tk.Label(frame1, image=tegla1N, bg='DarkSeaGreen2')
    labelT1.place(x=210,y=50)

    oBiljka1_1='1. Biljka je Orhideja, nalazi se \nu tegli:'
    oBiljka1=tk.StringVar()
    oBiljka1.set(oBiljka1_1)
    oBiljka1L=tk.Label(frame1,textvariable=oBiljka1, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oBiljka1L.place(x=155,y=0)

    oStatus1_1=f'Status: OK'
    oStatus1=tk.StringVar()
    oStatus1.set(oStatus1_1)
    oStatus1L=tk.Label(frame1,textvariable=oStatus1, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oStatus1L.place(x=155,y=130)

    detalji1Button=Button(frame1, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detalji1)
    detalji1Button.place(x=300, y=130)
     
    ################ Frame 2 ##############
    frame2 = tk.Frame(root, bg='DarkSeaGreen2', width=350, height=150)
    frame2.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

    image2 = Image.open(r'Slike\Biljke\Macuhice.jpg')
    image2 = image2.resize((150, 150), Image.ANTIALIAS)
    biljka2 = ImageTk.PhotoImage(image2)
    labelB2 = tk.Label(frame2, image=biljka2, bg='DarkSeaGreen2')
    labelB2.place(x=0, y=0)

    tegla2 = Image.open(r'Slike\Posude\Promjer9cm.jpg')
    tegla2R = tegla2.resize((70, 70), Image.ANTIALIAS)
    tegla2N = ImageTk.PhotoImage(tegla2R)
    labelT2 = tk.Label(frame2, image=tegla2N, bg='DarkSeaGreen2')
    labelT2.place(x=210,y=50)

    oBiljka2_1='2. Biljka je Macuhica, nalazi se \nu tegli:'
    oBiljka2=tk.StringVar()
    oBiljka2.set(oBiljka2_1)
    oBiljka2L=tk.Label(frame2,textvariable=oBiljka2, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oBiljka2L.place(x=155,y=0)

    oStatus2_1=f'Status: OK'
    oStatus2=tk.StringVar()
    oStatus2.set(oStatus2_1)
    oStatus2L=tk.Label(frame2,textvariable=oStatus2, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oStatus2L.place(x=155,y=130)

    detalji2Button=Button(frame2, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detalji2)
    detalji2Button.place(x=300, y=130)

    ############### Frame 3 ##############
    frame3 = tk.Frame(root, bg='DarkSeaGreen2', width=350, height=150)
    frame3.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

    image3 = Image.open(r'Slike\Biljke\Kaktus.webp')
    image3 = image3.resize((150, 150), Image.ANTIALIAS)
    biljka3 = ImageTk.PhotoImage(image3)
    labelB3 = tk.Label(frame3, image=biljka3, bg='DarkSeaGreen2')
    labelB3.place(x=0, y=0)

    tegla3 = Image.open(r'Slike\Posude\Promjer27cm.jpg')
    tegla3R = tegla3.resize((70, 70), Image.ANTIALIAS)
    tegla3N = ImageTk.PhotoImage(tegla3R)
    labelT3 = tk.Label(frame3, image=tegla3N, bg='DarkSeaGreen2')
    labelT3.place(x=210,y=50)

    oBiljka3_1='3. Biljka je Kaktus, nalazi se \nu tegli:'
    oBiljka3=tk.StringVar()
    oBiljka3.set(oBiljka3_1)
    oBiljka3L=tk.Label(frame3,textvariable=oBiljka3, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oBiljka3L.place(x=155,y=0)

    oStatus3_1=f'Status: OK'
    oStatus3=tk.StringVar()
    oStatus3.set(oStatus3_1)
    oStatus3L=tk.Label(frame3,textvariable=oStatus3, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oStatus3L.place(x=155,y=130)

    detalji3Button=Button(frame3, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detalji3)
    detalji3Button.place(x=300, y=130)

    ################### Frame 4 ################
    frame4 = tk.Frame(root, bg='DarkSeaGreen2', width=350, height=150)
    frame4.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

    image4 = Image.open(r'Slike\Biljke\FikusBenjamin.jpg')
    image4 = image4.resize((150, 150), Image.ANTIALIAS)
    biljka4 = ImageTk.PhotoImage(image4)
    labelB4 = tk.Label(frame4, image=biljka4, bg='DarkSeaGreen2')
    labelB4.place(x=0, y=0)

    tegla4 = Image.open(r'Slike\Posude\Promjer40cm.jpg')
    tegla4R = tegla4.resize((70, 70), Image.ANTIALIAS)
    tegla4N = ImageTk.PhotoImage(tegla4R)
    labelT4 = tk.Label(frame4, image=tegla4N, bg='DarkSeaGreen2')
    labelT4.place(x=210,y=50)

    oBiljka4_1='4. Biljka je Fikus Benjamin, \n nalazi se u tegli:'
    oBiljka4=tk.StringVar()
    oBiljka4.set(oBiljka4_1)
    oBiljka4L=tk.Label(frame4,textvariable=oBiljka4, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oBiljka4L.place(x=155,y=0)

    oStatus4_1=f'Status: OK'
    oStatus4=tk.StringVar()
    oStatus4.set(oStatus4_1)
    oStatus4L=tk.Label(frame4,textvariable=oStatus4, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oStatus4L.place(x=155,y=130)

    detalji4Button=Button(frame4, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detalji4)
    detalji4Button.place(x=300, y=130)

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=70)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=100)
    
    root.mainloop()

######################################## BUTTON POSUDE ###############################
def open_posude():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Biljke')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    #################  FRAME 1  ###############
    frame1 = tk.Frame(root, bg='DarkSeaGreen2', width=350, height=150)
    frame1.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

    image1 = Image.open(r'Slike\Posude\Promjer12cm.jpg')
    image1 = image1.resize((150, 150), Image.ANTIALIAS)
    tegla1 = ImageTk.PhotoImage(image1)
    labelT1 = tk.Label(frame1, image=tegla1, bg='DarkSeaGreen2')
    labelT1.place(x=0, y=0)

    biljka1 = Image.open(r'Slike/Biljke/Orhideja.jpg')
    biljka1R = biljka1.resize((70, 70), Image.ANTIALIAS)
    biljka1N = ImageTk.PhotoImage(biljka1R)
    labelB1 = tk.Label(frame1, image=biljka1N, bg='DarkSeaGreen2')
    labelB1.place(x=190,y=60)

    oTegla1_1='1. Posuda je bijela tegla za cvijece \n promjera 12 cm.\n U njoj je posadena Orhideja:'
    oTegla1=tk.StringVar()
    oTegla1.set(oTegla1_1)
    oTegla1L=tk.Label(frame1,textvariable=oTegla1, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oTegla1L.place(x=150,y=0)

    detaljiT1Button=Button(frame1, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detaljiT1)
    detaljiT1Button.place(x=300, y=130)
     
    ########################  FRAME 2  ###################
    frame2 = tk.Frame(root, bg='DarkSeaGreen2', width=350, height=150)
    frame2.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

    image2 = Image.open(r'Slike\Posude\Promjer9cm.jpg')
    image2 = image2.resize((150, 150), Image.ANTIALIAS)
    tegla2 = ImageTk.PhotoImage(image2)
    labelT2 = tk.Label(frame2, image=tegla2, bg='DarkSeaGreen2')
    labelT2.place(x=0, y=0)

    biljka2 = Image.open(r'Slike\Biljke\Macuhice.jpg')
    biljka2R = biljka2.resize((70, 70), Image.ANTIALIAS)
    biljka2N = ImageTk.PhotoImage(biljka2R)
    labelB2 = tk.Label(frame2, image=biljka2N, bg='DarkSeaGreen2')
    labelB2.place(x=190,y=60)

    oTegla2_1='2. Posuda je smeda tegla za cvijece \n promjera 9 cm.\n U njoj je posadena Macuhica:'
    oTegla2=tk.StringVar()
    oTegla2.set(oTegla2_1)
    oTegla2L=tk.Label(frame2,textvariable=oTegla2, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oTegla2L.place(x=150,y=0)

    detaljiT2Button=Button(frame2, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detaljiT2)
    detaljiT2Button.place(x=300, y=130)

    ######################  FRAME 3  ######################
    frame3 = tk.Frame(root, bg='DarkSeaGreen2', width=350, height=150)
    frame3.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

    image3 = Image.open(r'Slike\Posude\Promjer27cm.jpg')
    image3 = image3.resize((150, 150), Image.ANTIALIAS)
    tegla3 = ImageTk.PhotoImage(image3)
    labelT3 = tk.Label(frame3, image=tegla3, bg='DarkSeaGreen2')
    labelT3.place(x=0, y=0)

    biljka3 = Image.open(r'Slike\Biljke\Kaktus.webp')
    biljka3R = biljka3.resize((70, 70), Image.ANTIALIAS)
    biljka3N = ImageTk.PhotoImage(biljka3R)
    labelB3 = tk.Label(frame3, image=biljka3N, bg='DarkSeaGreen2')
    labelB3.place(x=190,y=60)

    oTegla3_1='3. Posuda je bijela tegla za cvijece \n promjera 27 cm.\n U njoj je posaden Kaktus:'
    oTegla3=tk.StringVar()
    oTegla3.set(oTegla3_1)
    oTegla3L=tk.Label(frame3,textvariable=oTegla3, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oTegla3L.place(x=150,y=0)

    detaljiT3Button=Button(frame3, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detaljiT3)
    detaljiT3Button.place(x=300, y=130)

    ######################  FRAME 4  ######################
    frame4 = tk.Frame(root, bg='DarkSeaGreen2', width=350, height=150)
    frame4.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

    image4 = Image.open(r'Slike\Posude\Promjer40cm.jpg')
    image4 = image4.resize((150, 150), Image.ANTIALIAS)
    tegla4 = ImageTk.PhotoImage(image4)
    labelT4 = tk.Label(frame4, image=tegla4, bg='DarkSeaGreen2')
    labelT4.place(x=0, y=0)

    biljka4 = Image.open(r'Slike\Biljke\FikusBenjamin.jpg')
    biljka4R = biljka4.resize((70, 70), Image.ANTIALIAS)
    biljka4N = ImageTk.PhotoImage(biljka4R)
    labelB4 = tk.Label(frame4, image=biljka4N, bg='DarkSeaGreen2')
    labelB4.place(x=190,y=60)

    oTegla4_1='4. Posuda je crna tegla za cvijece \n promjera 40 cm.\n U njoj je posaden Fikus Benjamin:'
    oTegla4=tk.StringVar()
    oTegla4.set(oTegla4_1)
    oTegla4L=tk.Label(frame4,textvariable=oTegla4, font=('Segoe UI',10), bg='DarkSeaGreen2', justify='left')
    oTegla4L.place(x=150,y=0)

    detaljiT4Button=Button(frame4, text="Detalji",width=7, font=('Helvetica bold',6), justify='right',bg='DarkSeaGreen2', command=open_detaljiT4)
    detaljiT4Button.place(x=300, y=130)

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=70)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=100)

    root.mainloop()

####################################### PROZOR NAKON LOGIRANJA ##########################################
def open_app():
    clearRoot(root)
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
    
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=800, y=10)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=800, y=40)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=800, y=70)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=800, y=100)

    root.mainloop()

############################    PRIJAVA    #############################
prijava=tk.Label(root,text="Prijava", font=('Calibri', 20), bg='DarkSeaGreen')
prijava.place(x=320, y=40)
korisnickoIme=tk.Label(root,text="Korisnicko ime", font=('Calibri', 15), bg='DarkSeaGreen')
korisnickoIme.place(x=320, y=80)
userName= Entry(root,show="",width=20, font=('Calibri', 15))
userName.place(x=320, y=110)
lozinka=tk.Label(root,text="Lozinka", font=('Calibri', 15), bg='DarkSeaGreen')
lozinka.place(x=320, y=140)
password= Entry(root,show="*",width=20, font=('Calibri', 15))
password.place(x=320, y=170)
loginButton=Button(root, text="Prijavi me",width=10, font=('Helvetica bold',13),command=login).place(x=320, y=205)
cancelButton=Button(root, text="Izlaz",width=10, font=('Helvetica bold',13),command=quit).place(x=320, y=240)

img1=Image.open("Slike/Login/Slika2_login.jpg")
img1R=img1.resize((200,200), Image.ANTIALIAS)
img1New= ImageTk.PhotoImage(img1R)
label=Label(root, image=img1New)
label.place(x=30, y=70)

root.mainloop()
