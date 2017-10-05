import csv

def score():
    with open('gamers.csv','r') as bestand:
        reader = csv.reader(bestand,delimiter=';')
        alle_scores = []
        for line in reader:
            alle_scores.append(int(line[2].strip()))
            # alle scores integer in alle_scores list
            highscore = max(alle_scores)
            # highscore bekend
        if str(highscore) in line[2]:
               print('De hoogste score is: {} op {} behaald door {}'.format(line[2],line[1],line[0]))

print(score())