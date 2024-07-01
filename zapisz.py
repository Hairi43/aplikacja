#!/usr/bin/python

import sqlite3
import csv
import datetime

# puste_id_adresu = -1;

def wykonaj_kod():

    conn = sqlite3.connect('dane')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS zebrane_dane (
            zuzycie float,
            data_odczytu date,
            id_domokrazcy int,
            ulica text not null,
            nr_budynku int,
            nr_mieszkania int,
            kod_pocztowy text not null,
            miejscowosc text not null
        )""")
    conn.commit()
    
    def Zapisz_dane_w_bazie(zuzycie, aktualna_data, id_domokrazcy, ulica, nr_budynku, nr_mieszkania, kod_pocztowy, miejscowosc):
        dane = [zuzycie, aktualna_data, id_domokrazcy, ulica, nr_budynku, nr_mieszkania, kod_pocztowy, miejscowosc]
        c.execute('INSERT INTO zebrane_dane VALUES (?,?,?,?,?,?,?,?)', dane)
        conn.commit()
    
    def Aktualizuj_w_bazie(zuzycie, aktualna_data, id_domokrazcy, ulica, nr_budynku, nr_mieszkania, kod_pocztowy, miejscowosc):
        dane = [zuzycie, aktualna_data, id_domokrazcy, ulica, nr_budynku, nr_mieszkania, kod_pocztowy, miejscowosc]
        c.execute('UPDATE zebrane_dane SET zuzycie = ?, data_odczytu = ?, id_domokrazcy = ? WHERE ulica = ? and nr_budynku = ? and nr_mieszkania = ? and kod_pocztowy = ? and miejscowosc = ?', dane) 
        conn.commit()
    
    koniec = True
    czyID = False
    print("Wpisz id domokrazcy")
    id_domokrazcy = input()
            
    while koniec:
    
        print("Wpisz ulicę")
        ulica = input()
    
        print("Wpisz nr budynku")
        nr_budynku = input()
    
        print("Wpisz nr mieszkania")
        nr_mieszkania = input()
        if nr_mieszkania == "":
            nr_mieszkania = None
    
        print("Wpisz kod pocztowy")
        kod_pocztowy = input()
    
        print("Wpisz miejscowość")
        miejscowosc = input()
    
        print("Wpisz zuzycie")
        zuzycie = input()
             
    
        for rekord in c.execute("""SELECT * FROM zebrane_dane"""):
            print(rekord[3], ulica, rekord[4], nr_budynku, rekord[5], nr_mieszkania, rekord[6], kod_pocztowy, rekord[7], miejscowosc)
            if str(rekord[3]) == str(ulica) and str(rekord[4]) == str(nr_budynku) and str(rekord[5]) == str(nr_mieszkania) and str(rekord[6]) == str(kod_pocztowy) and str(rekord[7]) == str(miejscowosc):
                czyID = True
        aktualna_data = datetime.datetime.now().strftime("%Y-%m-%d")
        if czyID is True:
            czyID = False
            print("podano adres, które już jest w bazie danych, czy chcesz zaaktualizować wpisane zuzycie?")
            print("wpisz t lub n")
            zaktualizuj = input()
            if zaktualizuj == "t":
                Aktualizuj_w_bazie(zuzycie, aktualna_data, id_domokrazcy, ulica, nr_budynku, nr_mieszkania, kod_pocztowy, miejscowosc)
                zaktualizuj = "n"
        else:
            Zapisz_dane_w_bazie(zuzycie, aktualna_data, id_domokrazcy, ulica, nr_budynku, nr_mieszkania, kod_pocztowy, miejscowosc)
        print("zakończyć wpisywanie? wpisz t jeśli tak, jeśli chcesz dalej wpisywać kliknij enter")
        sprawdz = input()
        
        if sprawdz == 't':
            koniec = False

    
    dane = []
    for rekord in c.execute("SELECT * FROM zebrane_dane"):
        dane.append(rekord)
        
    with open('zebrane_dane.csv', 'w') as plik:
        w = csv.writer(plik)
        w.writerow(['zuzycie', 'data_odczytu', 'id_domokrazcy', 'ulica', "nr_budynku", "nr_mieszkania", "kod_pocztowy", "miejscowosc"])
        w.writerows(dane)
        
        for rekord in c.execute("SELECT * FROM zebrane_dane"):
                print(rekord)
    
    conn.close()



if __name__ == "__main__":
    wykonaj_kod()
    