#################################### DETALJI --> POSUDE ####################################
def open_detalji_posuda(id):
    clearRoot(root)
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=850, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=850, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=850, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=850, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=850, y=130)

    # POVLACENJE PODATAKA O BILJCI PREKO plantId
    conn = sqlite3.connect('Baza_podataka.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Posude WHERE id=?", (id,))
    pot_data = c.fetchone()
    conn.close()

    # DODAVANJE ATRIBUTA NA PODATKE O BILJKAMA
    pot_name = pot_data[1]
    photo_image = pot_data[2]
    with open(photo_image, 'rb') as file:
        contents = file.read()
    photo = Image.open(io.BytesIO(contents))
    photo = photo.resize((150, 150), Image.ANTIALIAS)

    canvas = tk.Canvas(root, width=150, height=150)
    canvas.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
    photo = ImageTk.PhotoImage(photo)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    name_label = tk.Label(root, text=pot_name, font=("Arial", 14), bg="DarkSeaGreen2")
    name_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # pos_label = tk.Label(root, text=f"Pozicija: {polozaj}", font=("Arial", 12), bg="DarkSeaGreen2")
    # pos_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    # temp_label = tk.Label(root, text=f"Temperatura: {min_temp}°C - {max_temp}°C", font=("Arial", 12), bg="DarkSeaGreen2")
    # temp_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    # vlaz_label = tk.Label(root, text=f"Vlaznost: {min_vlaznost}% - {max_vlaznost}%", font=("Arial", 12), bg="DarkSeaGreen2")
    # vlaz_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    # svjet_label = tk.Label(root, text=f"Svjetlo: {min_svjetlost} - {max_svjetlost} lux", font=("Arial", 12), bg="DarkSeaGreen2")
    # svjet_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    # hrana_label = tk.Label(root, text=f"Hrana: {min_hrana} - {max_hrana}\n\n", font=("Arial", 12), bg="DarkSeaGreen2")
    # hrana_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    promjenaButton = tk.Button(root, text="Promjena podataka", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda: posuda_promjena_podataka(id))
    promjenaButton.grid(row=6, column=0, pady=(0, 10))

    izbrisiButton = tk.Button(root, text="Izbrisi biljku", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda: posuda_brisanje(id))
    izbrisiButton.grid(row=6, column=1, pady=(0, 10))


    root.mainloop()

#####################################
# class EntryWithPlaceholder(tk.Entry):
#     def __init__(self, master=None, placeholder="Enter text...", color='grey'):
#         super().__init__(master)
#         self.placeholder = placeholder
#         self.placeholder_color = color
#         self.default_fg_color = self['fg']
#         self.bind("<FocusIn>", self.on_focus_in)
#         self.bind("<FocusOut>", self.on_focus_out)
#         self.put_placeholder()

#     def put_placeholder(self):
#         self.insert(0, self.placeholder)
#         self['fg'] = self.placeholder_color

#     def remove_placeholder(self):
#         self.delete(0, tk.END)
#         self['fg'] = self.default_fg_color

#     def on_focus_in(self, event):
#         if self['fg'] == self.placeholder_color:
#             self.remove_placeholder()

    # def on_focus_out(self, event):
    #     if not self.get():
    #         self.put_placeholder()

################### PROMJENA PODATAKA BILJKE ###############
def posuda_promjena_podataka(id):
    clearRoot(root)
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=850, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=850, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=850, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=850, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=850, y=130)

    # POVLACENJE PODATAKA O BILJCI PREKO plantId
    conn = sqlite3.connect('Baza_podataka.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Posude WHERE id=?", (id,))
    plant_data = c.fetchone()
    conn.close()

    # DODAVANJE STRIBUTA PODACIMA O BILJKAMA
    pot_name = pot_data[1]
    photo_image = pot_data[2]
    with open(photo_image, 'rb') as file:
        contents = file.read()
    photo = Image.open(io.BytesIO(contents))
    photo = photo.resize((150, 150), Image.ANTIALIAS)

    canvas = tk.Canvas(root, width=150, height=150)
    canvas.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
    photo = ImageTk.PhotoImage(photo)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    name_label = tk.Label(root, text=pot_name, font=("Arial", 14), bg="DarkSeaGreen2")
    name_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    unos_name = EntryWithPlaceholder(root, pot_name, color="black")
    unos_name.grid(row=0, column=2, padx=10, pady=5)

    # pos_label = tk.Label(root, text=f"Pozicija: {polozaj}", font=("Arial", 12), bg="DarkSeaGreen2")
    # pos_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    # unos_name = EntryWithPlaceholder(root, polozaj, color="black")
    # unos_name.grid(row=1, column=2, padx=10, pady=5)

    # temp_label = tk.Label(root, text=f"Temperatura: {min_temp}°C {max_temp}°C", font=("Arial", 12), bg="DarkSeaGreen2")
    # temp_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    # unos_name = EntryWithPlaceholder(root, min_temp, color="black")
    # unos_name.grid(row=2, column=2, padx=10, pady=5)
    # unos_name = EntryWithPlaceholder(root, max_temp, color="black")
    # unos_name.grid(row=2, column=3, padx=10, pady=5)

    # vlaz_label = tk.Label(root, text=f"Vlaznost: {min_vlaznost}% - {max_vlaznost}%", font=("Arial", 12), bg="DarkSeaGreen2")
    # vlaz_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    # unos_name = EntryWithPlaceholder(root, min_vlaznost, color="black")
    # unos_name.grid(row=3, column=2, padx=10, pady=5)
    # unos_name = EntryWithPlaceholder(root, max_vlaznost, color="black")
    # unos_name.grid(row=3, column=3, padx=10, pady=5)

    # svjet_label = tk.Label(root, text=f"Svjetlost: {min_svjetlost} - {max_svjetlost} lux", font=("Arial", 12), bg="DarkSeaGreen2")
    # svjet_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    # unos_name = EntryWithPlaceholder(root, min_svjetlost, color="black")
    # unos_name.grid(row=4, column=2, padx=10, pady=5)
    # unos_name = EntryWithPlaceholder(root, max_svjetlost, color="black")
    # unos_name.grid(row=4, column=3, padx=10, pady=5)

    # hrana_label = tk.Label(root, text=f"Hrana: {min_hrana} - {max_hrana}", font=("Arial", 12), bg="DarkSeaGreen2")
    # hrana_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    # unos_name = EntryWithPlaceholder(root, min_hrana, color="black")
    # unos_name.grid(row=5, column=2, padx=10, pady=5)
    # unos_name = EntryWithPlaceholder(root, max_hrana, color="black")
    # unos_name.grid(row=5, column=3, padx=10, pady=5)

    promijeniSlikuButton = tk.Button(root, text="Ucitaj novu sliku", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=promijeni_sliku)
    promijeniSlikuButton.grid(row=6, column=1)

    spremiButton = tk.Button(root, text="Spremi", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=spremi_promjene)
    spremiButton.grid(row=6, column=0)

    root.mainloop()

##############################
# class EntryWithPlaceholder(tk.Entry):
#     def __init__(self, master=None, placeholder="Enter text...", color='grey'):
#         super().__init__(master)
#         self.placeholder = placeholder
#         self.placeholder_color = color
#         self.default_fg_color = self['fg']
#         self.bind("<FocusIn>", self.on_focus_in)
#         self.bind("<FocusOut>", self.on_focus_out)
#         self.put_placeholder()

#     def put_placeholder(self):
#         self.insert(0, self.placeholder)
#         self['fg'] = self.placeholder_color

#     def remove_placeholder(self):
#         self.delete(0, tk.END)
#         self['fg'] = self.default_fg_color

#     def on_focus_in(self, event):
#         if self['fg'] == self.placeholder_color:
#             self.remove_placeholder()

#     def on_focus_out(self, event):
#         if not self.get():
#             self.put_placeholder()

################ PROMJENA PODATAKA --> BILJKA ######################
def biljka_promjena_podataka(id):
    clearRoot(root)
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=850, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=850, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=850, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=850, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=850, y=130)

    # PODACI O BILJCI NA TEMELJU Id-a
    conn = sqlite3.connect('Baza_podataka.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Posude WHERE id=?", (id,))
    plant_data = c.fetchone()
    conn.close()

    # ATRIBUTI DODANI PODACIMA
    pot_name = pot_data[1]
    photo_image = pot_data[2]
    with open(photo_image, 'rb') as file:
        contents = file.read()
    photo = Image.open(io.BytesIO(contents))
    photo = photo.resize((150, 150), Image.ANTIALIAS)

    canvas = tk.Canvas(root, width=150, height=150)
    canvas.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
    photo = ImageTk.PhotoImage(photo)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    name_label = tk.Label(root, text=pot_name, font=("Arial", 14), bg="DarkSeaGreen2")
    name_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    unos_name = EntryWithPlaceholder(root, pot_name, color="black")
    unos_name.grid(row=0, column=2, padx=10, pady=5)

    # pos_label = tk.Label(root, text=f"Polozaj: {polozaj}", font=("Arial", 12), bg="DarkSeaGreen2")
    # pos_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    # unos_name = EntryWithPlaceholder(root, polozaj, color="black")
    # unos_name.grid(row=1, column=2, padx=10, pady=5)

    # temp_label = tk.Label(root, text=f"Temperatura: {min_temp}°C {max_temp}°C", font=("Arial", 12), bg="DarkSeaGreen2")
    # temp_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    # unos_name = EntryWithPlaceholder(root, min_temp, color="black")
    # unos_name.grid(row=2, column=2, padx=10, pady=5)
    # unos_name = EntryWithPlaceholder(root, max_temp, color="black")
    # unos_name.grid(row=2, column=3, padx=10, pady=5)

    # vlaz_label = tk.Label(root, text=f"Vlaznost: {min_vlaznost}% - {max_vlaznost}%", font=("Arial", 12), bg="DarkSeaGreen2")
    # vlaz_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    # unos_name = EntryWithPlaceholder(root, min_vlaznost, color="black")
    # unos_name.grid(row=3, column=2, padx=10, pady=5)
    # unos_name = EntryWithPlaceholder(root, max_vlaznost, color="black")
    # unos_name.grid(row=3, column=3, padx=10, pady=5)

    # svjet_label = tk.Label(root, text=f"Svjetlost: {min_svjetlost} - {max_svjetlost} lux", font=("Arial", 12), bg="DarkSeaGreen2")
    # svjet_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    # unos_name = EntryWithPlaceholder(root, min_svjetlost, color="black")
    # unos_name.grid(row=4, column=2, padx=10, pady=5)
    # unos_name = EntryWithPlaceholder(root, max_svjetlost, color="black")
    # unos_name.grid(row=4, column=3, padx=10, pady=5)

    # hrana_label = tk.Label(root, text=f"Hrana: {min_hrana} - {max_hrana}", font=("Arial", 12), bg="DarkSeaGreen2")
    # hrana_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    # unos_name = EntryWithPlaceholder(root, min_hrana, color="black")
    # unos_name.grid(row=5, column=2, padx=10, pady=5)
    # unos_name = EntryWithPlaceholder(root, max_hrana, color="black")
    # unos_name.grid(row=5, column=3, padx=10, pady=5)

    novaSlikaButton = tk.Button(root, text="Ucitaj novu sliku", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=promijeni_sliku)
    novaSlikaButton.grid(row=6, column=1)

    spremiButton = tk.Button(root, text="Spremi", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=spremi_promjene)
    spremiButton.grid(row=6, column=0)

    root.mainloop()

def posuda_brisanje(id):
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
    
###################### BOTUN DODAVANJA BILJKE --> SLIKA, POSUDA, SPREMI ##############
def dodaj_sliku():
    global dodajSlikuClicked
    global file_path
    file_path = filedialog.askopenfilename()
    dodajSlikuClicked = True
    if dodajSlikuClicked:
        try:
            with open(file_path, 'rb') as file:
                contents = file.read()
                posuda = Image.open(io.BytesIO(contents))
                posudaR = posuda.resize((150, 150), Image.ANTIALIAS)
                posudaN = ImageTk.PhotoImage(posudaR)
                label = tk.Label(root, image=posudaN, bg='DarkSeaGreen2')
                label.image = posudaN
                label.place(x=500, y=30)
                label.config(image=posudaN)
                dodajSlikuClicked = False
        except FileNotFoundError:
            print("File not found!")


def spremi(unosimePosude, file_path):
    global spremiClicked
    if(spremiClicked == True):
        unosimePosude_db = unosimePosude.get()
        
        create_table_query= '''CREATE TABLE IF NOT EXISTS Posude(
                                    id INTEGER PRIMARY KEY,
                                    unosimePosude_db TEXT NOT NULL,
                                    file_path STRING NOT NULL DEFAULT 0);'''
        database_name='Baza_podataka.db'

        try:
            sqliteConnection=sqlite3.connect(database_name)
            cursor=sqliteConnection.cursor()
            print(f'SQLite baza {database_name} je kreirana i spojena')
            cursor.execute(create_table_query)
            sqliteConnection.commit()       #commit primjenjuje nas upit
            print('Tabela vrijednosti dodana u bazu')
            cursor.close()
            print('CURSOR otpusten')
        except sqlite3.Error as error:
            print('Doslo je do pogreske prilikom spajanja na bazu: ', error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite verzija je zatvorena.')

        insert_into_table_query='''INSERT INTO Posude (unosimePosude, file_path)    
                                    VALUES (?,?)'''
            
        try:
            sqliteConnection=sqlite3.connect(database_name)
            cursor=sqliteConnection.cursor()
            print(f'SQLite baza {database_name} je kreirana i spojena')
            cursor.execute(insert_into_table_query, (unosimePosude, file_path))
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

####################### DODAJ POSUDU ##################
def dodaj_posudu():
    global dodajSlikuClicked
    global spremiClicked
    global file_path
    spremi_list = []
    clearRoot(root)
    root.title(f'PyFloraPosuda - Dodaj Posudu')
    root['bg'] = 'DarkSeaGreen2'
    root.geometry('900x500')

    naslovPosude=tk.Label(root,text="Unos nove posude", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=145, y=20)
    imePosude=tk.Label(root,text="Ime posude", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=20, y=70)
    unosimePosude = Entry(root,show="",width=20, font=('Calibri', 15))
    unosimePosude.place(x=150, y=70)
    vrijednostSenzora=tk.Label(root,text="Vrijednost senzora:", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=20, y=110)
    
    def sync_senzor():
        vlaga = random.randrange(30,70)
        oSenzor1=f'Senzor Vlage:\t{vlaga} %'
        oSenzor.set(oSenzor1)
        oSenzorL=tk.Label(root,textvariable=oSenzor, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
        oSenzorL.place(x=20,y=150)

        svjetlost = random.randrange(2500,6500)
        oSenzor1=f'Senzor Svjetla:\t{svjetlost} K'
        oSenzor.set(oSenzor1)
        oSenzorL=tk.Label(root,textvariable=oSenzor, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
        oSenzorL.place(x=185,y=70)

        hrana = random.randrange(0,100)
        oSenzor1=f'Senzor Hrane:\t{hrana} %'
        oSenzor.set(oSenzor1)
        oSenzorL=tk.Label(root,textvariable=oSenzor, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
        oSenzorL.place(x=185,y=105)

        temperatura = random.randrange(15,30)
        oSenzor1=f'Senzor temperature: {temperatura} °C'
        oSenzor.set(oSenzor1)
        oSenzorL=tk.Label(root,textvariable=oSenzor, font=('Segoe UI',15), bg='DarkSeaGreen2', justify='left')
        oSenzorL.place(x=185,y=140)

        global spremiClicked
        if(spremiClicked == True):            
            create_table_query= '''CREATE TABLE IF NOT EXISTS Senzori(
                                        id INTEGER PRIMARY KEY,
                                        dan TEXT NOT NULL,
                                        sat TEXT NOT NULL,
                                        vlaga TEXT NOT NULL,
                                        svjetlost INTEGER NOT NULL,
                                        hrana INTEGER NOT NULL,
                                        temeperatura INTEGER NOT NULL);'''
            database_name='Baza_podataka.db'

            try:
                sqliteConnection=sqlite3.connect(database_name)
                cursor=sqliteConnection.cursor()
                print(f'SQLite baza {database_name} je kreirana i spojena')
                cursor.execute(create_table_query)
                sqliteConnection.commit()       #commit primjenjuje nas upit
                print('Tabela vrijednosti dodana u bazu')
                cursor.close()
                print('CURSOR otpusten')
            except sqlite3.Error as error:
                print('Doslo je do pogreske prilikom spajanja na bazu: ', error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print('SQLite verzija je zatvorena.')

            insert_into_table_query='''INSERT INTO Senzori (mojaappdan, mojaappsat, vlaga, svjetlost, hrana, temperatura)    
                                        VALUES (?,?,?,?,?,?)'''
                
            try:
                sqliteConnection=sqlite3.connect(database_name)
                cursor=sqliteConnection.cursor()
                print(f'SQLite baza {database_name} je kreirana i spojena')
                cursor.execute(insert_into_table_query, (mojaappdan, mojaappsat, vlaga, svjetlost, hrana, temperatura))
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


    syncSenzorButton=Button(root, text="Sync senzor",width=10, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=sync_senzor).place(x=150, y=110)
    dodajSlikuButton=Button(root, text="Dodaj sliku",width=10, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=dodaj_sliku).place(x=20, y=380)
    dodajBiljkuButton=Button(root, text="Dodaj biljku",width=10, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=dodaj_biljku).place(x=110, y=380)
    spremiButton=Button(root, text="Spremi",width=10, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command= lambda:[switchClicked(), spremi(unosimePosude, file_path) ]).place(x=200, y=380)

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=750, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=750, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=750, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=750, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=750, y=130)

    root.mainloop()

###################### SLAGANJE STRANICE POSUDE ############## 
class PlantCard(tk.Frame):
    def __init__(self, parent, potId, tk_instance):
        self.photo = None
        self.tk_instance = tk_instance
        super().__init__(parent, bg='DarkSeaGreen2', highlightbackground="gray", highlightthickness=1)
        self.plantId = potId
        self.load_pot_data()
        self.create_widgets()

    #################### KREIRENJE WIDGETA --> POSUDE #########
    def create_widgets(self):
        # SLIKA POSUDE
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # CANVAS ZA SLIKU POSUDE
        self.canvas = tk.Canvas(self, width=150, height=150)
        self.canvas.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
        self.photo = ImageTk.PhotoImage(self.photo)
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        detaljiButton = tk.Button(self, text="Detalji", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda: open_detalji_posuda(self.plantId))
        detaljiButton.grid(row=5, column=0, pady=(0, 10))

        name_label = tk.Label(self, text=self.pot_name, font=("Arial", 14), bg='DarkSeaGreen2')
        name_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # pos_label = tk.Label(self, text=f"Pozicija: {self.polozaj}", font=("Arial", 12), bg='DarkSeaGreen2')
        # pos_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # temp_label = tk.Label(self, text=f"Temperatura: {self.min_temp}°C - {self.max_temp}°C", font=("Arial", 12), bg='DarkSeaGreen2')
        # temp_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # vlaz_label = tk.Label(self, text=f"Vlaznost: {self.min_vlaznost}% - {self.max_vlaznost}%", font=("Arial", 12), bg='DarkSeaGreen2')
        # vlaz_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # svjet_label = tk.Label(self, text=f"Svjetlost: {self.min_svjetlost} - {self.max_svjetlost} lux", font=("Arial", 12), bg='DarkSeaGreen2')
        # svjet_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # hrana_label = tk.Label(self, text=f"Hrana: {self.min_hrana} - {self.max_hrana}", font=("Arial", 12), bg='DarkSeaGreen2')
        # hrana_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        # PROVJERITI SIRI LI SE WIDGET S KARTICOM BILJKE KAKO BI ISPUNIO SIRINU ZASLONA
        self.columnconfigure(1, weight=1)

        # Create a scrollbar and connect it to the Canvas widget
        # scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        # scrollbar.grid(row=0, column=1, sticky="ns")
        # self.canvas.configure(yscrollcommand=scrollbar.set)


    def yview(self, *args):
        self.canvas.yview(*args)

    ############## DOHVACANJE PODATAKA IZ BAZE --> POSUDE #######
    def load_pot_data(self):
        # DOHVACANJE PODATAKA PREKO ID-a
        conn = sqlite3.connect('Baza_podataka.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Posude WHERE id=?", (self.potId,))
        pot_data = c.fetchone()
        conn.close()

        # POSTAVITI ATRIBUTE ZA PODATKE O BILJKAMA
        pot_name = pot_data[1]
        photo_image = pot_data[2]
        with open(self.photo_image, 'rb') as file:
            contents = file.read()
        self.photo = Image.open(io.BytesIO(contents))
        self.photo = self.photo.resize((150, 150), Image.ANTIALIAS)

#########################################  BUTTON POSUDE   ##################################
def open_posude():
    clearRoot(root)
    root.title(f'PyFloraPosuda - Posude')
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
    pot_cards_frame = tk.Frame(canvas, bg="DarkSeaGreen2")

    # KRAIRATI FRAME KOJI CE ZADRZATI PlantCard UNUTAR CANVASA
    pot_cards_frame = tk.Frame(canvas, bg="DarkSeaGreen2")
    canvas.create_window((0, 0),window=pot_cards_frame, anchor="nw")

    # POVLACENJE BAZE PODATAKA
    conn = sqlite3.connect('Baza_podataka.db')

    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Posude'")
    table_exists = cursor.fetchone() is not None

    if table_exists:
        # IZVRSITI UPIT ZA ODABIR SVIH PODATAKA IZ TABLICE Posude
        cursor.execute("SELECT * FROM Posude")

        # DOHVACANJE REZULTATA
        pot_data = cursor.fetchall()

        # CREIRANJE LISTE ZA DODAVANJE BILJAKA --> PlantCard
        pot_cards = []

        # CREIRANJE PlantCard-a ZA SVAKU BILJKU I DODAVANJE NA LISTU
        for data in pot_data:
            pot_card = PotCard(pot_cards_frame, data[0], tk_instance=root)
            pot_cards.append(po_card)

        # SLAGANJE PlantCard-a U DVIJE KOLONE
        row = 0
        column = 0
        for i, pot_card in enumerate(pot_cards):
            pot_card.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
            column += 1
            if column == 2:
                column = 0
                row += 1

        # UPDETANJE SCROLLBAR-a
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
    else:
        dodaj_posudu

    # ZATVARANJE BAZE PODATAKA
    conn.close()

    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=850, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=850, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=850, y=70)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=850, y=100)

    dodajButton=Button(root, text="Dodaj posudu",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=dodaj_posudu).place(x=850, y=150)
     
    root.mainloop()