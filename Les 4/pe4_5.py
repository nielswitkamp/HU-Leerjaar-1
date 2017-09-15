grondgetallen = [4, 5, 3, -81]

def kwadraten_som(x):
    res = 0
    for x in grondgetallen:
        if x >= 0:
            res = (x**2)+res
    print(res)
print(kwadraten_som(grondgetallen))