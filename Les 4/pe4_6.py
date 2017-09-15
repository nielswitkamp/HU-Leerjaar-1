lijst = ['a', 'b', 'c']
def wijzig(x):
    del lijst[:]
lijst = ['d', 'e', 'f']
print(lijst)

#Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
    #omdat de lijst al bestaat

#Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
    #waarschijnlijk wel, in mijn geval word de lijst volledig verwijderd en opnieuw aangemaakt.

#Welke rol speelt (im)mutabiliteit in deze vraag?
    #Om ervoor te zorgen dat je jouw lijsten altijd nog kan aanpassen.
