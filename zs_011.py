import io
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import urllib.request
from PIL import Image, ImageTk
from urllib.request import urlopen
import json
import sqlite3
from datetime import date, datetime
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np
spremiClicked = False
file_path = ""
dodajSlikuClicked = False

def switchClicked():
    global spremiClicked
    if(spremiClicked == True):
        spremiClicked = False
    else:
        spremiClicked = True

now=datetime.now()
mojaappdan=now.strftime("%d.%m.%Y.")
mojaappsat=now.strftime("%H:%M:%S")

urljson=f'https://api.tutiempo.net/json/?lan=en&apid=zwDX4azaz4X4Xqs&ll=43.51436051979722,16.444448215112512'
response=urlopen(urljson)
data_json=json.loads(response.read())

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
def open_detalji_biljka(id):
    clearRoot(root)
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=850, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=850, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=850, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=850, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=850, y=130)

    # Retrieve plant data from the database using plantId
    conn = sqlite3.connect('Baza_podataka.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Biljke WHERE id=?", (id,))
    plant_data = c.fetchone()
    conn.close()

    # Set attributes for plant data
    plant_name = plant_data[1]
    polozaj = plant_data[2]
    min_temp = plant_data[3]
    max_temp = plant_data[4]
    min_vlaznost = plant_data[5]
    max_vlaznost = plant_data[6]
    min_svjetlost = plant_data[7]
    max_svjetlost = plant_data[8]
    min_hrana = plant_data[9]
    max_hrana = plant_data[10]
    photo_image = plant_data[11]
    with open(photo_image, 'rb') as file:
        contents = file.read()
    photo = Image.open(io.BytesIO(contents))
    photo = photo.resize((150, 150), Image.ANTIALIAS)

    canvas = tk.Canvas(root, width=150, height=150)
    canvas.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
    photo = ImageTk.PhotoImage(photo)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    name_label = tk.Label(root, text=plant_name, font=("Arial", 14), bg="DarkSeaGreen2")
    name_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    pos_label = tk.Label(root, text=f"Pozicija: {polozaj}", font=("Arial", 12), bg="DarkSeaGreen2")
    pos_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    temp_label = tk.Label(root, text=f"Temperatura: {min_temp}°C - {max_temp}°C", font=("Arial", 12), bg="DarkSeaGreen2")
    temp_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    vlaz_label = tk.Label(root, text=f"Vlaznost: {min_vlaznost}% - {max_vlaznost}%", font=("Arial", 12), bg="DarkSeaGreen2")
    vlaz_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    svjet_label = tk.Label(root, text=f"Svjetlo: {min_svjetlost} - {max_svjetlost} lux", font=("Arial", 12), bg="DarkSeaGreen2")
    svjet_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    hrana_label = tk.Label(root, text=f"Hrana: {min_hrana} - {max_hrana}\n\n", font=("Arial", 12), bg="DarkSeaGreen2")
    hrana_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    detaljiButton = tk.Button(root, text="Promjena podataka", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda: biljka_promjena_podataka(id))
    detaljiButton.grid(row=6, column=0, pady=(0, 10))

    detaljiButton = tk.Button(root, text="Izbrisi biljku", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda: biljka_brisanje(id))
    detaljiButton.grid(row=6, column=1, pady=(0, 10))

    root.mainloop()

import tkinter as tk

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="Enter text...", color='grey'):
        super().__init__(master)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def remove_placeholder(self):
        self.delete(0, tk.END)
        self['fg'] = self.default_fg_color

    def on_focus_in(self, event):
        if self['fg'] == self.placeholder_color:
            self.remove_placeholder()

    def on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()


def biljka_promjena_podataka(id):
    clearRoot(root)
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=850, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=850, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=850, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=850, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=850, y=130)

    # Retrieve plant data from the database using plantId
    conn = sqlite3.connect('Baza_podataka.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Biljke WHERE id=?", (id,))
    plant_data = c.fetchone()
    conn.close()

    # Set attributes for plant data
    plant_name = plant_data[1]
    polozaj = plant_data[2]
    min_temp = plant_data[3]
    max_temp = plant_data[4]
    min_vlaznost = plant_data[5]
    max_vlaznost = plant_data[6]
    min_svjetlost = plant_data[7]
    max_svjetlost = plant_data[8]
    min_hrana = plant_data[9]
    max_hrana = plant_data[10]
    photo_image = plant_data[11]
    with open(photo_image, 'rb') as file:
        contents = file.read()
    photo = Image.open(io.BytesIO(contents))
    photo = photo.resize((150, 150), Image.ANTIALIAS)

    canvas = tk.Canvas(root, width=150, height=150)
    canvas.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
    photo = ImageTk.PhotoImage(photo)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    name_label = tk.Label(root, text=plant_name, font=("Arial", 14), bg="DarkSeaGreen2")
    name_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    unos_name = EntryWithPlaceholder(root, plant_name, color="black")
    unos_name.grid(row=0, column=2, padx=10, pady=5)

    pos_label = tk.Label(root, text=f"Position: {polozaj}", font=("Arial", 12), bg="DarkSeaGreen2")
    pos_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    unos_name = EntryWithPlaceholder(root, polozaj, color="black")
    unos_name.grid(row=1, column=2, padx=10, pady=5)

    temp_label = tk.Label(root, text=f"Temperature: {min_temp}°C {max_temp}°C", font=("Arial", 12), bg="DarkSeaGreen2")
    temp_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    unos_name = EntryWithPlaceholder(root, min_temp, color="black")
    unos_name.grid(row=2, column=2, padx=10, pady=5)
    unos_name = EntryWithPlaceholder(root, max_temp, color="black")
    unos_name.grid(row=2, column=3, padx=10, pady=5)

    vlaz_label = tk.Label(root, text=f"Humidity: {min_vlaznost}% - {max_vlaznost}%", font=("Arial", 12), bg="DarkSeaGreen2")
    vlaz_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    unos_name = EntryWithPlaceholder(root, min_vlaznost, color="black")
    unos_name.grid(row=3, column=2, padx=10, pady=5)
    unos_name = EntryWithPlaceholder(root, max_vlaznost, color="black")
    unos_name.grid(row=3, column=3, padx=10, pady=5)

    svjet_label = tk.Label(root, text=f"Light: {min_svjetlost} - {max_svjetlost} lux", font=("Arial", 12), bg="DarkSeaGreen2")
    svjet_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    unos_name = EntryWithPlaceholder(root, min_svjetlost, color="black")
    unos_name.grid(row=4, column=2, padx=10, pady=5)
    unos_name = EntryWithPlaceholder(root, max_svjetlost, color="black")
    unos_name.grid(row=4, column=3, padx=10, pady=5)

    hrana_label = tk.Label(root, text=f"Nutrients: {min_hrana} - {max_hrana}", font=("Arial", 12), bg="DarkSeaGreen2")
    hrana_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    unos_name = EntryWithPlaceholder(root, min_hrana, color="black")
    unos_name.grid(row=5, column=2, padx=10, pady=5)
    unos_name = EntryWithPlaceholder(root, max_hrana, color="black")
    unos_name.grid(row=5, column=3, padx=10, pady=5)

    detaljiButton = tk.Button(root, text="Ucitaj novu sliku", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda: biljka_brisanje(id))
    detaljiButton.grid(row=6, column=1)

    detaljiButton = tk.Button(root, text="Spremi", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda: biljka_promjena_podataka(id))
    detaljiButton.grid(row=6, column=0)

    root.mainloop()

def biljka_brisanje(id):
    quit

    hrana_label = tk.Label(root, text=f"Nutrients: {min_hrana} - {max_hrana}\n\n", font=("Arial", 12), bg="DarkSeaGreen2")
    hrana_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    promjenaPodatakaButton = tk.Button(root, text="Promjena podataka", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda: biljka_promjena_podataka(id))
    promjenaPodatakaButton.grid(row=6, column=0, pady=(0, 10))

    brisanjeButton = tk.Button(root, text="Izbrisi biljku", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda: biljka_brisanje(id))
    brisanjeButton.grid(row=6, column=1, pady=(0, 10))

    root.mainloop()

import tkinter as tk

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="Enter text...", color='grey'):
        super().__init__(master)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def remove_placeholder(self):
        self.delete(0, tk.END)
        self['fg'] = self.default_fg_color

    def on_focus_in(self, event):
        if self['fg'] == self.placeholder_color:
            self.remove_placeholder()

    def on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()


def biljka_promjena_podataka(id):
    clearRoot(root)
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=850, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=850, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=850, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=850, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=850, y=130)

    # PODACI O BILJCI NA TEMELJI Id-a
    conn = sqlite3.connect('Baza_podataka.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Biljke WHERE id=?", (id,))
    plant_data = c.fetchone()
    conn.close()

    # ATRIBUTI DODANI PODACIMA
    plant_name = plant_data[1]
    polozaj = plant_data[2]
    min_temp = plant_data[3]
    max_temp = plant_data[4]
    min_vlaznost = plant_data[5]
    max_vlaznost = plant_data[6]
    min_svjetlost = plant_data[7]
    max_svjetlost = plant_data[8]
    min_hrana = plant_data[9]
    max_hrana = plant_data[10]
    photo_image = plant_data[11]
    with open(photo_image, 'rb') as file:
        contents = file.read()
    photo = Image.open(io.BytesIO(contents))
    photo = photo.resize((150, 150), Image.ANTIALIAS)

    canvas = tk.Canvas(root, width=150, height=150)
    canvas.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
    photo = ImageTk.PhotoImage(photo)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    name_label = tk.Label(root, text=plant_name, font=("Arial", 14), bg="DarkSeaGreen2")
    name_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    unos_name = EntryWithPlaceholder(root, plant_name, color="black")
    unos_name.grid(row=0, column=2, padx=10, pady=5)

    pos_label = tk.Label(root, text=f"Polozaj: {polozaj}", font=("Arial", 12), bg="DarkSeaGreen2")
    pos_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    unos_name = EntryWithPlaceholder(root, polozaj, color="black")
    unos_name.grid(row=1, column=2, padx=10, pady=5)

    temp_label = tk.Label(root, text=f"Temperatura: {min_temp}°C {max_temp}°C", font=("Arial", 12), bg="DarkSeaGreen2")
    temp_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    unos_name = EntryWithPlaceholder(root, min_temp, color="black")
    unos_name.grid(row=2, column=2, padx=10, pady=5)
    unos_name = EntryWithPlaceholder(root, max_temp, color="black")
    unos_name.grid(row=2, column=3, padx=10, pady=5)

    vlaz_label = tk.Label(root, text=f"Vlaznost: {min_vlaznost}% - {max_vlaznost}%", font=("Arial", 12), bg="DarkSeaGreen2")
    vlaz_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    unos_name = EntryWithPlaceholder(root, min_vlaznost, color="black")
    unos_name.grid(row=3, column=2, padx=10, pady=5)
    unos_name = EntryWithPlaceholder(root, max_vlaznost, color="black")
    unos_name.grid(row=3, column=3, padx=10, pady=5)

    svjet_label = tk.Label(root, text=f"Svjetlost: {min_svjetlost} - {max_svjetlost} lux", font=("Arial", 12), bg="DarkSeaGreen2")
    svjet_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    unos_name = EntryWithPlaceholder(root, min_svjetlost, color="black")
    unos_name.grid(row=4, column=2, padx=10, pady=5)
    unos_name = EntryWithPlaceholder(root, max_svjetlost, color="black")
    unos_name.grid(row=4, column=3, padx=10, pady=5)

    hrana_label = tk.Label(root, text=f"Hrana: {min_hrana} - {max_hrana}", font=("Arial", 12), bg="DarkSeaGreen2")
    hrana_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    unos_name = EntryWithPlaceholder(root, min_hrana, color="black")
    unos_name.grid(row=5, column=2, padx=10, pady=5)
    unos_name = EntryWithPlaceholder(root, max_hrana, color="black")
    unos_name.grid(row=5, column=3, padx=10, pady=5)

    novaSlikaButton = tk.Button(root, text="Ucitaj novu sliku", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=promijeni_sliku)
    novaSlikaButton.grid(row=6, column=1)

    spremiButton = tk.Button(root, text="Spremi", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=spremi_promjene)
    spremiButton.grid(row=6, column=0)

    root.mainloop()

def biljka_brisanje(id):
    quit

def spremi_promjene():
    quit

def promijeni_sliku():
    quit

######################################## GRAFOVI #######################################
def open_line():
    quit
    # root = tk.Tk()
    # root.title("Line Chart")

    # fig = Figure(figsize=(7,1.5), dpi=100)
    # x = np.linspace(0, 10, 100)
    # y = np.sin(x)
    # ax = fig.add_subplot(111)
    # ax.plot(x, y)

    # canvas = FigureCanvasTkAgg(fig, master=root)
    # canvas.draw()
    # canvas.get_tk_widget().pack()

    # tk.mainloop()

def open_pie():
    quit
    # cars = ['AUDI', 'BMW', 'FORD',
    #     'TESLA', 'JAGUAR', 'MERCEDES']
 
    # data = [23, 17, 35, 29, 12, 41]
        
    # # Creating plot
    # fig = plt.figure(figsize =(7,1))
    # plt.pie(data, labels = cars)
        
    # # show plot
    # plt.show()

def open_histo():
    quit

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

    lineButton=Button(root, text="Line",width=10, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_line).place(x=480, y=250)
    pieButton=Button(root, text="Pie",width=10, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=open_pie).place(x=560, y=250)
    histoButton=Button(root, text="Histo",width=10, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=open_histo).place(x=640, y=250)

    root.mainloop()
    
###################### BOTUNI DODAVANJA BILJKE ##############
def dodaj_sliku():
    global dodajSlikuClicked
    global file_path
    file_path = filedialog.askopenfilename()
    dodajSlikuClicked = True
    if dodajSlikuClicked:
        try:
            with open(file_path, 'rb') as file:
                contents = file.read()
                biljka = Image.open(io.BytesIO(contents))
                biljkaR = biljka.resize((150, 150), Image.ANTIALIAS)
                biljkaN = ImageTk.PhotoImage(biljkaR)
                label = tk.Label(root, image=biljkaN, bg='DarkSeaGreen2')
                label.image = biljkaN
                label.place(x=500, y=30)
                label.config(image=biljkaN)
                dodajSlikuClicked = False
        except FileNotFoundError:
            print("File not found!")


def dodaj_posudu():
    quit

def spremi(unosimeBiljke, unospolozajBiljke, unosmintemp, unosmaxtemp, unosminVlaznost, unosmaxVlaznost, unosminSvjetlost, unosmaxSvjetlost, unosminHrana, unosmaxHrana, file_path):
    global spremiClicked
    if(spremiClicked == True):
        unosimeBiljke_db = unosimeBiljke.get()
        unospolozajBiljke_db = unospolozajBiljke.get()
        unosmintemp_db = unosmintemp.get()
        unosmaxtemp_db = unosmaxtemp.get()
        unosminVlaznost_db = unosminVlaznost.get()
        unosmaxVlaznost_db = unosmaxVlaznost.get()
        unosminSvjetlost_db = unosminSvjetlost.get()
        unosmaxSvjetlost_db = unosmaxSvjetlost.get()
        unosminHrana_db = unosminHrana.get()
        unosmaxHrana_db = unosmaxHrana.get()
        create_table_query= '''CREATE TABLE IF NOT EXISTS Biljke(
                                    id INTEGER PRIMARY KEY,
                                    unosimeBiljke_db TEXT NOT NULL,
                                    unospolozajBiljke_db TEXT NOT NULL,
                                    unosmintemp_db INTEGER NOT NULL,
                                    unosmaxtemp_db INTEGER NOT NULL,
                                    unosminVlaznost_db INTEGER NOT NULL,
                                    unosmaxVlaznost_db INTEGER NOT NULL,
                                    unosminSvjetlost_db INTEGER NOT NULL,
                                    unosmaxSvjetlost_db INTEGER NOT NULL,
                                    unosminHrana_db INTEGER NOT NULL,
                                    unosmaxHrana_db INTEGER NOT NULL,
                                    file_path STRING NOT NULL DEFAULT 0);'''
        database_name='Baza_podataka.db'

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

        insert_into_table_query='''INSERT INTO Biljke (unosimeBiljke_db, unospolozajBiljke_db, unosmintemp_db, unosmaxtemp_db, unosminVlaznost_db, unosmaxVlaznost_db, unosminSvjetlost_db, unosmaxSvjetlost_db, unosminHrana_db, unosmaxHrana_db, file_path)    
                                    VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
            
        try:
            sqliteConnection=sqlite3.connect(database_name)
            cursor=sqliteConnection.cursor()
            print(f'SQLite baza {database_name} je kreirana i spojena')
            cursor.execute(insert_into_table_query, (unosimeBiljke_db, unospolozajBiljke_db, unosmintemp_db, unosmaxtemp_db, unosminVlaznost_db, unosmaxVlaznost_db, unosminSvjetlost_db, unosmaxSvjetlost_db, unosminHrana_db, unosmaxHrana_db, file_path))
            sqliteConnection.commit()
            cursor.close()
            print('CURSOR otpusten')
        except sqlite3.Error as error:
            print('Doslo je do pogreske prilikom spajanja na bazu: ', error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite verzija je zatvorena.')
        switchClicked()
####################### DODAJ BILJKU ##################
def dodaj_biljku():
    global dodajSlikuClicked
    global spremiClicked
    global file_path
    spremi_list = []
    clearRoot(root)
    root.title(f'PyFloraPosuda - Dodaj Biljku')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    naslovBiljke=tk.Label(root,text="Unos nove biljke", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=145, y=20)
    imeBiljke=tk.Label(root,text="Ime biljke", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=20, y=70)
    unosimeBiljke = Entry(root,show="",width=20, font=('Calibri', 15))
    unosimeBiljke.place(x=150, y=70)
    polozajBiljke=tk.Label(root,text="Polozaj u kuci", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=20, y=110)
    unospolozajBiljke = Entry(root,show="",width=20, font=('Calibri', 15))
    unospolozajBiljke.place(x=150, y=110)
    odrzavanjeBiljke=tk.Label(root,text="Odrzavanje:", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=20, y=150)
    minTemp=tk.Label(root,text="Min. temp.°C", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=20, y=190)
    unosmintemp = Entry(root,show="",width=7, font=('Calibri', 15))
    unosmintemp.place(x=170, y=190)
    maxTemp=tk.Label(root,text="Max. temp.°C", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=250, y=190)
    unosmaxtemp = Entry(root,show="",width=7, font=('Calibri', 15))
    unosmaxtemp.place(x=390, y=190)
    minVlaznost=tk.Label(root,text="Min. vlaznost %", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=20, y=230)
    unosminVlaznost = Entry(root,show="",width=7, font=('Calibri', 15))
    unosminVlaznost.place(x=170, y=230)
    maxVlaznost=tk.Label(root,text="Max. vlaznost %", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=250, y=230)
    unosmaxVlaznost = Entry(root,show="",width=7, font=('Calibri', 15))
    unosmaxVlaznost.place(x=390, y=230)
    minSvjetlost=tk.Label(root,text="Min. svjetlost K", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=20, y=270)
    unosminSvjetlost = Entry(root,show="",width=7, font=('Calibri', 15))
    unosminSvjetlost.place(x=170, y=270)
    maxSvjetlost=tk.Label(root,text="Max. svjetlost K", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=250, y=270)
    unosmaxSvjetlost = Entry(root,show="",width=7, font=('Calibri', 15))
    unosmaxSvjetlost.place(x=390, y=270)
    minHrana=tk.Label(root,text="Min. ishrana %", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=20, y=310)
    unosminHrana = Entry(root,show="",width=7, font=('Calibri', 15))
    unosminHrana.place(x=170, y=310)
    maxHrana=tk.Label(root,text="Max. ishrana %", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=250, y=310)
    unosmaxHrana = Entry(root,show="",width=7, font=('Calibri', 15))
    unosmaxHrana.place(x=390, y=310)

    dodajSlikuButton=Button(root, text="Dodaj sliku",width=10, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=dodaj_sliku).place(x=20, y=380)
    dodajPosuduButton=Button(root, text="Dodaj posudu",width=10, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=dodaj_posudu).place(x=110, y=380)
    spremiButton=Button(root, text="Spremi",width=10, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command= lambda:[switchClicked(), spremi(unosimeBiljke, unospolozajBiljke, unosmintemp, unosmaxtemp, unosminVlaznost, unosmaxVlaznost, unosminSvjetlost, unosmaxSvjetlost, unosminHrana, unosmaxHrana, file_path) ]).place(x=200, y=380)

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=130)

    root.mainloop()

###################### SLAGANJE STRANICE BILJKE ############## 
class PlantCard(tk.Frame):
    def __init__(self, parent, plantId, tk_instance):
        self.photo = None
        self.tk_instance = tk_instance
        super().__init__(parent, bg='DarkSeaGreen2', highlightbackground="gray", highlightthickness=1)
        self.plantId = plantId
        self.load_plant_data()
        self.create_widgets()

    #################### KREIRENJE WIDGETA --> BILJKE #########
    def create_widgets(self):
        # SLIKA BILJKE
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # CANVAS ZA SLIKU BILJKE
        self.canvas = tk.Canvas(self, width=150, height=150)
        self.canvas.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
        self.photo = ImageTk.PhotoImage(self.photo)
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        detaljiButton = tk.Button(self, text="Detalji", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda: open_detalji_biljka(self.plantId))
        detaljiButton.grid(row=5, column=0, pady=(0, 10))

        name_label = tk.Label(self, text=self.plant_name, font=("Arial", 14), bg='DarkSeaGreen2')
        name_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        pos_label = tk.Label(self, text=f"Pozicija: {self.polozaj}", font=("Arial", 12), bg='DarkSeaGreen2')
        pos_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        temp_label = tk.Label(self, text=f"Temperatura: {self.min_temp}°C - {self.max_temp}°C", font=("Arial", 12), bg='DarkSeaGreen2')
        temp_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        vlaz_label = tk.Label(self, text=f"Vlaznost: {self.min_vlaznost}% - {self.max_vlaznost}%", font=("Arial", 12), bg='DarkSeaGreen2')
        vlaz_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        svjet_label = tk.Label(self, text=f"Svjetlost: {self.min_svjetlost} - {self.max_svjetlost} lux", font=("Arial", 12), bg='DarkSeaGreen2')
        svjet_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        hrana_label = tk.Label(self, text=f"Hrana: {self.min_hrana} - {self.max_hrana}", font=("Arial", 12), bg='DarkSeaGreen2')
        hrana_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        # PROVJERITI SIRI LI SE WIDGET S KARTICOM BILJKE KAKO BI ISPUNIO SIRINU ZASLONA
        self.columnconfigure(1, weight=1)

        # Create a scrollbar and connect it to the Canvas widget
        # scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        # scrollbar.grid(row=0, column=1, sticky="ns")
        # self.canvas.configure(yscrollcommand=scrollbar.set)


    def yview(self, *args):
        self.canvas.yview(*args)

    ############## DOHVACANJE PODATAKA IZ BAZE --> BILJKE #######
    def load_plant_data(self):
        # DOHVACANJE PODATAKA PREKO ID-a
        conn = sqlite3.connect('Baza_podataka.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Biljke WHERE id=?", (self.plantId,))
        plant_data = c.fetchone()
        conn.close()

        # POSTAVITI ATRIBUTE ZA PODATKE O BILJKAMA
        self.plant_name = plant_data[1]
        self.polozaj = plant_data[2]
        self.min_temp = plant_data[3]
        self.max_temp = plant_data[4]
        self.min_vlaznost = plant_data[5]
        self.max_vlaznost = plant_data[6]
        self.min_svjetlost = plant_data[7]
        self.max_svjetlost = plant_data[8]
        self.min_hrana = plant_data[9]
        self.max_hrana = plant_data[10]
        self.photo_image = plant_data[11]
        with open(self.photo_image, 'rb') as file:
            contents = file.read()
        self.photo = Image.open(io.BytesIO(contents))
        self.photo = self.photo.resize((150, 150), Image.ANTIALIAS)

#########################################  BUTTON BILJKE   ##################################
def open_biljke():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Biljke')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('1000x500')

    ###### CANVAS --> SCROLLBAR ############33
    canvas = tk.Canvas(root, bg="DarkSeaGreen2")
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # POZICIJA CANVASA
    canvas.pack(side="left", fill="both", expand=True)

    # FEAME NA CANVASU
    plant_cards_frame = tk.Frame(canvas, bg="DarkSeaGreen2")

    # KRAIRATI FRAME KOJI CE ZADRZATI PlantCard UNUTAR CANVASA
    plant_cards_frame = tk.Frame(canvas, bg="DarkSeaGreen2")
    canvas.create_window((0, 0),window=plant_cards_frame, anchor="nw")

    # POVLACENJE BAZE PODATAKA
    conn = sqlite3.connect('Baza_podataka.db')

    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Biljke'")
    table_exists = cursor.fetchone() is not None

    if table_exists:
        # IZVRSITI UPIT ZA ODABIR SVIH PODATAKA IZ TABLICE BILJKE
        cursor.execute("SELECT * FROM Biljke")

        # DOHVACANJE REZULTATA
        plant_data = cursor.fetchall()

        # CREIRANJE LISTE ZA DODAVANJE BILJAKA --> PlantCard
        plant_cards = []

        # CREIRANJE PlantCard-a ZA SVAKU BILJKU I DODAVANJE NA LISTU
        for data in plant_data:
            plant_card = PlantCard(plant_cards_frame, data[0], tk_instance=root)
            plant_cards.append(plant_card)

        # SLAGANJE PlantCard-a U DVIJE KOLONE
        row = 0
        column = 0
        for i, plant_card in enumerate(plant_cards):
            plant_card.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
            column += 1
            if column == 2:
                column = 0
                row += 1

        # UPDETANJE SCROLLBAR-a
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
    else:
        dodaj_biljku

    # ZATVARANJE BAZE PODATAKA
    conn.close()

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=850, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=850, y=40)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=850, y=70)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=850, y=100)

    dodajButton=Button(root, text="Dodaj biljku",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=dodaj_biljku).place(x=850, y=150)
     
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

    root.mainloop()

####################################### VREMENSKA PROGNOZA ##########################################
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