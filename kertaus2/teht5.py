def suurin_arvo(luku1, luku2, luku3):
    if luku1 >= luku2 and luku1 >= luku3:
        return luku1
    elif luku2 >= luku1 and luku2 >= luku3:
        return luku2
    else:
        return luku3

a = float(input("anna ensimmäinen luku: "))
b = float(input("anna toinen luku: "))
c = float(input("anna kolmas luku: "))

tulos = suurin_arvo(a, b, c)
print(f"suurin luku on: {tulos}")