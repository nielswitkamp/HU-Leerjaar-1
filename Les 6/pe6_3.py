invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
def sp(invoer):
    splits = invoer.split('-')
    nieuwe_lijst = []
    for x in splits:
        y = int(x)
        nieuwe_lijst.append(y)
    return  (nieuwe_lijst)
print('Gesorteerde list van ints:',sp(invoer))
print('Grootste getal is:',max(sp(invoer)),'Het kleinste getal is:',min(sp(invoer)))
print('Aantal getallen:',len(sp(invoer)),'en de Som van de getallen:', sum(sp(invoer)) )
print('Gemiddelde:',sum(sp(invoer))/len(sp(invoer)))
