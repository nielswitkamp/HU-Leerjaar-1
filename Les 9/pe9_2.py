import datetime
import csv

def inloggers():
    bestand = open('inloggers.csv','w',newline='')
    writer = csv.writer(bestand,delimiter=';')
    writer.writerow(('datum','naam','voorl','gbdatum','email'))
    datum = datetime.datetime.today()

    while True:
        naam = input("Wat is je achternaam? ")
        if naam == '':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        writer.writerow((datum, naam, voorl, gbdatum, email))
    bestand.close()
print(inloggers())