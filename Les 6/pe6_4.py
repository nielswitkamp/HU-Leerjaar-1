studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    antw = []
    for line in studentencijfers:
        som = sum(line) / len(line)
        antw.append([som])
    return antw
print ('Het gemiddelde per student:',gemiddelde_per_student(studentencijfers))

def gemiddelde_van_alle_studenten(studentencijfers):
    for line in studentencijfers:
        som = sum(line)
        aantal_studenten = sum(len(line) for line in studentencijfers)
        antw = som / aantal_studenten
        return antw
print('Het gemiddelde van alle studenten is:',gemiddelde_van_alle_studenten(studentencijfers))
