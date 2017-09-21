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
    if weekendrit(weekend):
        if int(leeftijd) <=65 and leeftijd > 12 :
            return (standaardprijs(afstandKM) - standaardprijs(afstandKM) * 0.30)
        return (standaardprijs(afstandKM) - standaardprijs(afstandKM) * 0.35)
    else:
        if leeftijd <= 65 and leeftijd > 12:
            return (standaardprijs(afstandKM))
        return (standaardprijs(afstandKM) - standaardprijs(afstandKM) * 0.40)

print('Uw reis heeft u: €',ritprijs(int(leeftijd),weekendrit,float(afstandKM)),'gekost')