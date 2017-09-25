maand = input('geef de maand:')
def seizoen(x):
    if int(maand) >= 3 and int(maand) <= 5:
        return 'lente'
    elif int(maand) >= 6 and int(maand) <= 8:
        return 'zomer'
    elif int(maand) >= 9 and int(maand) <= 11:
        return 'herfst'
    elif int(maand) == 12 or int(maand) <= 2:
        return 'winter'
print(seizoen(maand))