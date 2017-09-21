infile = open('d:/HU/Programmeren/Opdrachten/Files/kaartnummers.txt', 'r')
def mlg(inputfile):
    for line in inputfile:
        x = line.split(', ')
        print (x[1].strip(), 'Heeft als kaartnummer:',x[0].strip())
mlg(infile)
infile.close()