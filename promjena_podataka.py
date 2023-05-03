def spremi_promjene_biljke(plant_id, unos_name, unos_pozicija, unos_min_temp, unos_max_temp, unos_min_vlaznost, unos_max_vlaznost, unos_min_svjetlost, unos_max_svjetlost, unos_min_hrana, unos_max_hrana, file_path):
    unosimeBiljke_new = unos_name.get()
    unospolozajBiljke_new = unos_pozicija.get()
    unosmintemp_new = unos_min_temp.get()
    unosmaxtemp_new = unos_max_temp.get()
    unosminVlaznost_new = unos_min_vlaznost.get()
    unosmaxVlaznost_new = unos_max_vlaznost.get()
    unosminSvjetlost_new = unos_min_svjetlost.get()
    unosmaxSvjetlost_new = unos_max_svjetlost.get()
    unosminHrana_new = unos_min_hrana.get()
    unosmaxHrana_new = unos_max_hrana.get()
    
    #SPAJANJE NA DB
    conn = sqlite3.connect('Baza_podataka.db')
    c = conn.cursor()

    # UPDATE DB
    c.execute(f"UPDATE Biljke SET unosimeBiljke_db = '{unosimeBiljke_new}', unospolozajBiljke_db = '{unospolozajBiljke_new}', unosmintemp_db = '{unosmintemp_new}', unosmaxtemp_db = '{unosmaxtemp_new}', unosminVlaznost_db = '{unosminVlaznost_new}', unosmaxVlaznost_db = '{unosmaxVlaznost_new}', unosminSvjetlost_db = '{unosminSvjetlost_new}', unosmaxSvjetlost_db = '{unosmaxSvjetlost_new}', unosminHrana_db = '{unosminHrana_new}', unosmaxHrana_db = '{unosmaxHrana_new}' , file_path = '{file_path}' WHERE id = '{plant_id}'")
    conn.commit()
    conn.close()
    open_biljke()

################### PROMJENA PODATAKA BILJKE ###############
def biljka_promjena_podataka(id):
    global file_path
    clearRoot(root)
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=850, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=850, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=850, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=850, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=850, y=130)

    # POVLACENJE PODATAKA O BILJCI PREKO plantId
    conn = sqlite3.connect('Baza_podataka.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Biljke WHERE id=?", (id,))
    plant_data = c.fetchone()
    conn.close()

    # DODAVANJE STRIBUTA PODACIMA O BILJKAMA
    plant_id = plant_data[0]
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
    file_path = plant_data[11]
    with open(file_path, 'rb') as file:
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

    pos_label = tk.Label(root, text=f"Pozicija: {polozaj}", font=("Arial", 12), bg="DarkSeaGreen2")
    pos_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    unos_pozicija = EntryWithPlaceholder(root, polozaj, color="black")
    unos_pozicija.grid(row=1, column=2, padx=10, pady=5)

    temp_label = tk.Label(root, text=f"Temperatura: {min_temp}°C {max_temp}°C", font=("Arial", 12), bg="DarkSeaGreen2")
    temp_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    unos_min_temp = EntryWithPlaceholder(root, min_temp, color="black")
    unos_min_temp.grid(row=2, column=2, padx=10, pady=5)
    unos_max_temp = EntryWithPlaceholder(root, max_temp, color="black")
    unos_max_temp.grid(row=2, column=3, padx=10, pady=5)

    vlaz_label = tk.Label(root, text=f"Vlaznost: {min_vlaznost}% - {max_vlaznost}%", font=("Arial", 12), bg="DarkSeaGreen2")
    vlaz_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    unos_min_vlaznost = EntryWithPlaceholder(root, min_vlaznost, color="black")
    unos_min_vlaznost.grid(row=3, column=2, padx=10, pady=5)
    unos_max_vlaznost = EntryWithPlaceholder(root, max_vlaznost, color="black")
    unos_max_vlaznost.grid(row=3, column=3, padx=10, pady=5)

    svjet_label = tk.Label(root, text=f"Svjetlost: {min_svjetlost} - {max_svjetlost} lux", font=("Arial", 12), bg="DarkSeaGreen2")
    svjet_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    unos_min_svjetlost = EntryWithPlaceholder(root, min_svjetlost, color="black")
    unos_min_svjetlost.grid(row=4, column=2, padx=10, pady=5)
    unos_max_svjetlost = EntryWithPlaceholder(root, max_svjetlost, color="black")
    unos_max_svjetlost.grid(row=4, column=3, padx=10, pady=5)

    hrana_label = tk.Label(root, text=f"Hrana: {min_hrana} - {max_hrana}", font=("Arial", 12), bg="DarkSeaGreen2")
    hrana_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    unos_min_hrana = EntryWithPlaceholder(root, min_hrana, color="black")
    unos_min_hrana.grid(row=5, column=2, padx=10, pady=5)
    unos_max_hrana = EntryWithPlaceholder(root, max_hrana, color="black")
    unos_max_hrana.grid(row=5, column=3, padx=10, pady=5)

    promijeniSlikuButton = tk.Button(root, text="Ucitaj novu sliku", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=promijeni_sliku)
    promijeniSlikuButton.grid(row=6, column=1)

    spremiButton = tk.Button(root, text="Spremi", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda: spremi_promjene_biljke(plant_id,unos_name, unos_pozicija, unos_min_temp, unos_max_temp, unos_min_vlaznost, unos_max_vlaznost, unos_min_svjetlost, unos_max_svjetlost, unos_min_hrana, unos_max_hrana, file_path))
    spremiButton.grid(row=6, column=0)

    root.mainloop()

def spremi_promjene_posude(posuda_id, unosPosuda, file_path):
    unosimePosuda_new = unosPosuda.get()
    #SPAJANJE NA DB
    conn = sqlite3.connect('Baza_podataka.db')
    c = conn.cursor()

    # UPDATE DB
    c.execute(f"UPDATE Posude SET unosimePosude_db = '{unosimePosuda_new}', file_path = '{file_path}' WHERE id = '{posuda_id}'")
    conn.commit()
    conn.close()
    open_posude()

    ################### PROMJENA PODATAKA POSUDE ###############
def posuda_promjena_podataka(id):
    clearRoot(root)
    pocetnaButton=Button(root, text="Pocetna stranica",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_app).place(x=850, y=10)
    mojProfilButton=Button(root, text="Moj profil",width=15, font=('Helvetica bold',10), justify='right', bg='DarkSeaGreen2', command=open_profil).place(x=850, y=40)
    biljkeButton=Button(root, text="Biljke",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_biljke).place(x=850, y=70)
    posudeButton=Button(root, text="Posude",width=15, font=('Helvetica bold',10), justify='right' ,bg='DarkSeaGreen2', command=open_posude).place(x=850, y=100)
    cancelButton=Button(root, text="Izlaz",width=15, font=('Helvetica bold',10), justify='right',bg='DarkSeaGreen2', command=quit).place(x=850, y=130)

    # POVLACENJE PODATAKA O POSUDI PREKO potId
    conn = sqlite3.connect('Baza_podataka.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Posude WHERE id=?", (id,))
    pot_data = c.fetchone()
    conn.close()

    # DODAVANJE ATRIBUTA PODACIMA O POSUDAMA
    pot_id = pot_data[0]
    pot_name = pot_data[1]
    plant_id = pot_data[2]
    photo_image = pot_data[3]
    with open(photo_image, 'rb') as file:
        contents = file.read()
    photo = Image.open(io.BytesIO(contents))
    photo = photo.resize((150, 150), Image.ANTIALIAS)

    conn = sqlite3.connect('Baza_podataka.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Biljke'")
    table_exists = cursor.fetchone()
    plant_list_name = []
    if table_exists:
        cursor.execute("SELECT * FROM Biljke")
        # DOHVACANJE REZULTATA
        plant_data = cursor.fetchall()
        # CREIRANJE LISTE ZA DODAVANJE BILJAKA U POSUDE --> PlantList
        plant_list_id = []
        # CREIRANJE PlantCard-a ZA SVAKU BILJKU I DODAVANJE NA LISTU
        plant_list_name = []
        for data in plant_data:
            print(data)
            plant_list_id.append(data[0])
            plant_list_name.append(data[1])

    biljka = tk.Label(root, text="Dodaj biljku", font=('Calibri', 15), bg='DarkSeaGreen2').place(x=20, y=100)
    odabranaBiljka = ttk.Combobox(root, values=plant_list_name)
    odabranaBiljka.place(x=150, y=100)
    
    def save_posuda():
        selected_plant_index = odabranaBiljka.current()
        selected_plant_id = plant_list_id[selected_plant_index]
        spremi_posudu(unosimePosude, selected_plant_id, file_path)

    canvas = tk.Canvas(root, width=150, height=150)
    canvas.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
    photo = ImageTk.PhotoImage(photo)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    name_label = tk.Label(root, text=pot_name, font=("Arial", 14), bg="DarkSeaGreen2")
    name_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    unos_nameP = EntryWithPlaceholder(root, pot_name, color="black")
    unos_nameP.grid(row=0, column=2, padx=10, pady=5)

    promijeniSlikuButton = tk.Button(root, text="Ucitaj novu sliku", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=promijeni_sliku)
    promijeniSlikuButton.grid(row=6, column=1)

    spremiButton = tk.Button(root, text="Spremi", width=15, font=('Helvetica bold', 10), justify='center', bg='DarkSeaGreen2', anchor=tk.S, command=lambda:spremi_promjene_posude(pot_id, unos_nameP, file_path))
    spremiButton.grid(row=6, column=0)

    root.mainloop()