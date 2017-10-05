def reis():
    try:
        aantal_personen = input('Met hoeveel personen gaat u op reis:')
        int_aantal = int(aantal_personen)
        gedeelde_prijs = 4356/int_aantal
        if int_aantal <= 0:
            raise AssertionError
        else:
            print('de reis kost {} euro per persoon'.format(gedeelde_prijs))
    except AssertionError:
        print('negatieve getallen zijn niet toegestaan')
    except ZeroDivisionError:
        print('delen door nul kan niet!')
    except ValueError:
        print('gebruik cijfers voor de invoer van het aantal')
    except:
        print('onjuiste invoer')
print(reis())