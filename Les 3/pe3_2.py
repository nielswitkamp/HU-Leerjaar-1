leeftijd = int(input('Geef je leeftijd'))
paspoort = input('Bent u in het bezit van een Nederlands paspoort?')
if int(leeftijd) >= 18 and paspoort == 'ja' or paspoort == 'Ja':
    print ('Gefeliciteerd u mag stemmen!')