nieuw_wachtwoord = input(('Geef een nieuw wachtwoord:'))
oud_wachtwoord = input(('Geef uw oude wachtwoord:'))
def new_password(x):
    if x == oud_wachtwoord and len(nieuw_wachtwoord) < 6:
        return ('False')
    else:
        return ('True')
print(new_password(nieuw_wachtwoord))