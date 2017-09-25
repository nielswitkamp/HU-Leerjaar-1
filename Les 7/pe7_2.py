while True:
    invoer = input('Geef een string van vier letters:')
    if len(invoer) > 4 or len(invoer) < 4:
        print(invoer,'heeft',len(invoer),'letters')
    else:
        break