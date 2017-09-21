def regels(x):
    infile = open('d:/HU/Programmeren/Opdrachten/Files/kaartnummers.txt','r')
    lineList = infile.readlines()
    infile.close()
    return (len(lineList))
print('Deze file telt',regels('kaartnummers.txt'),'regels')

def nummers(x):
    infile = open('d:/HU/Programmeren/Opdrachten/Files/kaartnummers.txt','r')
    inhoud = infile.readlines()
    grootste = max(inhoud)
    infile.close()
    if grootste in inhoud:
        print('Het grootste kaartnummer is:',grootste[:6],'en dat staat op regel:',inhoud.index(grootste)+1)

print(nummers('kaartnummers.txt'))