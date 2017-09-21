zin = input('Geef uw zin:')
woorden = zin.split()
gemiddelde = sum(len(woorden) for woorden in woorden)/len(woorden)
print (gemiddelde)