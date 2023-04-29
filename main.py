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
import main_window
#print(data_json)

root = tk.Tk()
root.title(f'PyFloraPosuda aplikacija - Prijava')
root['bg'] = 'DarkSeaGreen'
root.geometry('600x450')

now=datetime.now()
mojaappdan=now.strftime("%d.%m.%Y.")
mojaappsat=now.strftime("%H:%M:%S")

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
        main_window.open_app()
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

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=main_window.open_app).place(x=750, y=10)
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
    
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=main_window.open_app).place(x=750, y=10)
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

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=main_window.open_app).place(x=750, y=10)
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
     
####################################### PROZOR NAKON LOGIRANJA ##########################################

main_window.open_app(root)
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