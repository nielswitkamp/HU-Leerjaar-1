from pydoc import doc

import xmltodict

def lezen_xml():
    with open('final_stations','r') as bestand:
        doc = xmltodict.parse(bestand.read())
        codes = ""
        types = ""
        print('Dit zijn de codes en types van de 4 stations')
        for codes_types in doc['Stations']['Station']:
            codes = (codes_types['Code'])
            types = (codes_types['Type'])
            print('{:5} - {}'.format(codes,types))

        print('\n''Dit zijn de stations met één of meer synoniemen')
        synoniem = ""
        for codes_synoniemen in doc['Stations']['Station']:
            if codes_synoniemen['Synoniemen']:
                synoniem = (codes_synoniemen['Synoniemen']['Synoniem'])
                print('{:5} - {}'.format(codes,synoniem))

        print('\n''Dit is de langen naam van elk station')
        lange_naam = ""
        for codes_naam in doc['Stations']['Station']:
            lange_naam = (codes_naam['Namen']['Lang'])
            print ('{:5} - {}'.format(codes,lange_naam))

lezen_xml()