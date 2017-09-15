lengte = int(input('Geef uw lengte:'))
def lang_genoeg(x):
    if x >= 120:
        return ('je bent lang genoeg voor de attractie')
    else:
        return ("Sorry, je bent te klein!")
print(lang_genoeg(lengte))