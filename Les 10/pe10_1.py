import xmltodict

def lezen_xml():
    with open('d:/HU/Programmeren/Opdrachten/Files/artikelen.xml','r') as fd:
        doc = xmltodict.parse(fd.read())
        artikel_namen = {}
        for artikelen in doc['artikelen']['artikel']:
            artikel_namen = artikelen
            print(artikel_namen['naam'])
lezen_xml()