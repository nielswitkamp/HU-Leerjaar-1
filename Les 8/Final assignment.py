stations = ['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam amstel','Utrecht Centraal',"'s-Hertogenbosch",'Eindhoven','Weert','Roermond','Sittard','Maastricht']

def inlezen_beginstation(stations):
    while True:
        station = input('Geef uw beginstation:')
        if station not in stations:
            print ('Deze trein komt niet in',station)

        else:
            #print('Uw beginstation:', station)
            break
    return stations.index(station)

def inlezen_eindstation(stations,beginstation_index):
    while True:
        eindstation = input('Geef uw eindstation:')
        if eindstation not in stations:
            print('Deze trein komt niet in',eindstation)

        else:
            #print('Uw eindstation:', eindstation)
            eind_index = stations.index(eindstation)
            if eind_index > beginstation_index:
                return stations.index(eindstation)
            else:
                print('Eindstation ligt voor beginstation')

def omroepen_reis(stations,beginstation_index,eindstation_index):
    print('Het beginstation',stations[beginstation_index],'is het',beginstation_index+1,'station in het traject')
    print('Het eindstation',stations[eindstation_index],'is het',eindstation_index+1)
    print('De afstand bedraagd',eindstation_index - beginstation_index,'station(s)')
    print('De prijs van het kaartje is',(eindstation_index - beginstation_index)*5,'euro','\n')
    print('Jij stapt in de trein in:',stations[beginstation_index])
    for x in stations[beginstation_index+1:eindstation_index]:
        print('- ',x)
    #print(stations[beginstation_index+1:eindstation_index])
    print('Jij stapt uit de trein in:',stations[eindstation_index])

beginstation_index = inlezen_beginstation(stations)
eindstation_index = inlezen_eindstation(stations, beginstation_index)
omroepen_reis(stations,beginstation_index,eindstation_index)