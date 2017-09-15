afstandKM = input('Hoeveel km is de trein rit:')

def standaardprijs(x):
    if float(afstandKM) <= 0 :
        print ('De trein rit heeft u niets gekost!')
    if float(afstandKM) >= 0 and float(afstandKM) <= 50:
        normaal = float(afstandKM)*float(0.8)
        return normaal
    if float(afstandKM) >= 50:
        groter = float(afstandKM)*float(0.6) + 15
        return groter


weekend = input('Op welke dag reist u:')
def weekendrit(x):
    if weekend == 'zaterdag' or weekend == 'zondag':
        return True
    else:
        return False



leeftijd = input('Geef uw leeftijd:')

def ritprijs(leeftijd,weekendrit,afstandKM):
    if int(leeftijd) < 12 and weekendrit(weekend):
        tariefmetkorting2 = float(standaardprijs(afstandKM)) - float(standaardprijs(afstandKM) / 100) * 35
        return (tariefmetkorting2)
    if int(leeftijd) >= 65 and weekendrit(weekend):
        tariefmetkorting2 = float(standaardprijs(afstandKM)) - float(standaardprijs(afstandKM) / 100) * 35
        return (tariefmetkorting2)
    if int(leeftijd) >= 65:
        tariefmetkorting1 = float(standaardprijs(afstandKM)) - float(standaardprijs(afstandKM) / 100) * 30
        return (tariefmetkorting1)
    if int(leeftijd) < 12:
        tariefmetkorting1 = float(standaardprijs(afstandKM)) - float(standaardprijs(afstandKM) / 100) * 30
        return (tariefmetkorting1)
    if int(leeftijd) >= 12 and weekendrit(weekend):
        tariefmetkorting3 = float(standaardprijs(afstandKM)) - float(standaardprijs(afstandKM) / 100) * 40
        return (tariefmetkorting3)
    if int(leeftijd) < 65 and weekendrit(weekend):
        tariefmetkorting3 = float(standaardprijs(afstandKM)) - float(standaardprijs(afstandKM) / 100) * 40
        return (tariefmetkorting3)
    if int(leeftijd) >= 12 :
        return (standaardprijs(afstandKM))
    if int(leeftijd) < 65 :
        return (standaardprijs(afstandKM))
print('Uw reis heeft u: €',ritprijs(leeftijd,weekendrit,afstandKM),'gekost')