import csv
def schrijven_bestand():
    with open('artikellen.csv','w',newline='') as bestand:
        writer = csv.writer(bestand,delimiter=';')
        writer.writerow(('Artikelnummer','Artikelcode','Naam','Voorraad','Prijs'))

        while True:
            Artikelnummer = input("Geef het artikelnummer: ")
            if Artikelnummer == '':
                break
            Artikelcode = input("Geef de artikelcode: ")
            Naam = input("Geef de naam van het product: ")
            Voorraad = input("Hoeveel zijn er op voorraad: ")
            Prijs = float(input("Hoeveel kost het product?"))
            writer.writerow((Artikelnummer, Artikelcode, Naam, Voorraad, Prijs))
#print(schrijven_bestand())

def lezen_bestand():
    with open('artikellen.csv', 'r', newline='') as bestand:
        reader = csv.DictReader(bestand,delimiter=';')
        duurste_product = {"Prijs" : "0.0"}
        minste_product = {"Voorraad" : 10000 }
        alle_producten = []
        for product in reader:
            if float(product['Prijs']) >  float(duurste_product['Prijs']):
                duurste_product = product
            if int(product['Voorraad']) < int(minste_product['Voorraad']):
                minste_product = product
            alle_producten.append(int(product['Voorraad']))
        som_alle_producten = sum(alle_producten)
        print('Het duurste product is:',duurste_product['Naam'],'en die kost',duurste_product['Prijs'],'euro')
        print('Er zijn slechts:',minste_product['Voorraad'],'exemplaren in voorraad van het product met nummer:',minste_product['Artikelnummer'])
        print('In totaal hebben wij:',som_alle_producten,'producten in ons magazijn liggen')
lezen_bestand()