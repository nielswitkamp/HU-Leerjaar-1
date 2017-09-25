# kluizen = open('d:/HU/Programmeren/Opdrachten/Files/kluizen.txt', 'r+')
# inhoud =  kluizen.readlines()
max_kluizen = 12


def aantal_kluizen_vrij():
    kluizen = lees_kluizen()
    return (max_kluizen - len(kluizen))


def lees_kluizen():
    bestand = open('d:/HU/Programmeren/Opdrachten/Files/kluizen.txt', 'r')
    kluizen = bestand.readlines()
    kluisnummers_in_gebruik = []
    for kluis in kluizen:
        kluislist = kluis.strip().split(';')
        kluisnummers_in_gebruik.append([int(kluislist[0]), kluislist[1]])
    bestand.close()
    return kluisnummers_in_gebruik


def schrijven_kluizen(kluizen):
    bestand = open('d:/HU/Programmeren/Opdrachten/Files/kluizen.txt', 'w')
    for kluis in kluizen:
        bestand.writelines(str(kluis[0]) + ';' + kluis[1] + '\n')
    bestand.close()


def nieuwe_kluis():
    kluizen = lees_kluizen()
    # zoeken naar beschikbare kluis
    if len(kluizen) < max_kluizen:
        for kluisnummer in range(1, max_kluizen + 1):
            found = False
            # kluis zoeken
            for kluis in kluizen:
                if kluis[0] == kluisnummer:
                    found = True
                    break
            if found == False:
                break
        # lege kluis gevonden ja
        kluis = []
        wachtwoord = wachtwoord_kluize()
        kluis.append(kluisnummer)
        kluis.append(wachtwoord)
        kluizen.append(kluis)
        print('U heeft kluis nummer:', kluisnummer, 'met als wachtwoord:', wachtwoord)
        schrijven_kluizen(kluizen)
    else:
        print('Geen kluis beschikbaar')


def wachtwoord_kluize():
    return input('Geef uw kluis code:')


def kluis_openen():
    kluizen = lees_kluizen()
    kluisnummer = int(input('Geef uw kluisnummer:'))
    wachtwoord = input('Geef uw wachtwoord:')
    invoer = [int(kluisnummer), str(wachtwoord)]
    for line in kluizen:
        if invoer in kluizen:
            return 'Uw kluis is geopend'
        else:
            return ' Onjuist wachtwoord of kluisnummer'


menu = True
while menu:
    print("""
    1. ik wil weten hoeveel kluizen er nog vrij zijn
    2. ik wil een nieuwe kluis
    3. ik wil even iets uit mijn kluis halen
    4. ik geef mijn kluis terug
    5. ik wil stoppen
    """"")
    menu = input("Wat wilt u gaan doen:")
    if menu == "1":
        print('\n', 'Er zijn nog:', aantal_kluizen_vrij(), 'kluizen vrij')
    elif menu == "2":
        print('\n', nieuwe_kluis())
    elif menu == "3":
        print('\n', kluis_openen())
    elif menu == "4":
        print('\n', 'Geef kluis terug: optioneel')
    elif menu == "5":
        break
    else:
        print('Ongeldige keuze')