def ticker():
    bestand = open('d:/HU/Programmeren/Opdrachten/Files/ticker.txt','r')
    bedrijven = bestand.readlines()
    for line in bedrijven:
        lijst = line.strip().split(':')
        namen = lijst[0]
        tickers = lijst[1]
        dict = {}
        dict[namen] = tickers
        bestand.close()

def zoeken_ticker():
    bestand = open('d:/HU/Programmeren/Opdrachten/Files/ticker.txt','r')
    bedrijven = bestand.readlines()
    while True:
        bedrijfsnaam = input('Enter Company name:')
        for line in bedrijven:
            lijst = line.strip().split(':')
            if bedrijfsnaam in lijst:
                print('Ticker symbol:',lijst[1])
        tickernaam = input('Enter Ticker symbol:')
        for line in bedrijven:
            lijst = line.strip().split(':')
            if tickernaam in lijst:
                print('Company name:',lijst[0])
        break

print(zoeken_ticker())
