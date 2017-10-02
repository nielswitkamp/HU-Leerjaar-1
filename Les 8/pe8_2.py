import random
def monopolyworp():
    for getal in range(1):
        randomNR1 = random.randint(1, 6)
        randomNR2 = random.randint(1, 6)
        som = randomNR1+randomNR2

        if randomNR1 == randomNR2:
            print(randomNR1,'+',randomNR2,'=',som,'(dubbel)')
            randomNR3 = random.randint(1,6)
            randomNR4 = random.randint(1,6)
            som = randomNR3+randomNR4
            if randomNR3 == randomNR4:
                print(randomNR3,'+',randomNR4,'=',som,'(dubbel)')
                randomNR5 = random.randint(1,6)
                randomNR6 = random.randint(1,6)
                som = randomNR5+randomNR6
                if randomNR5 == randomNR6:
                    print(randomNR5,'+',randomNR6,'=',som,'(direct door naar de gevangenis)')
                else:
                    print(randomNR5,'+',randomNR6,'=',som)
            else:
                print(randomNR3,'+',randomNR4,'=',som)
        else:
            print(randomNR1,'+',randomNR2,'=',som)

print(monopolyworp())
