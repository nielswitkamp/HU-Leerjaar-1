lijst = eval(input('Geef lijst met minimaal 10 strings:'))
nieuwe_lijst = []
for woorden in lijst:
    if len(woorden) == 4:
        nieuwe_lijst.append(str(woorden))
print('De nieuwe lijst met 4 letter woorden is:',nieuwe_lijst)