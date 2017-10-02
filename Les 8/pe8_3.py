def code():
    invoer = input('gebruiker+beginstation+eindstation:')
    uitkomst = ""
    for letter in invoer:
        verander = chr(ord(letter)+3)
        uitkomst = uitkomst+verander
    return uitkomst
print(code())

