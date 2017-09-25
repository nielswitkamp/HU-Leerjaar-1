count= {}

while True:

    name = input('Volgende naam:')
    lst = name.split()

    for n in lst:
        count[n] = count.get(n, 0) + 1

    if not lst:
        for n in count:
            if count[n] == 1:
                print('Er is {} student met de naam {}'.format(count[n],n))
            else:
                print('Er zijn {} studenten met de naam {}'.format(count[n],n))
        break