nimet = set()

while True:
    nimi = input("anna nimiä: (tyhjä lopettaa) ")
    if nimi == "":
        break
    if nimi in nimet:
        print("aiemmin syötetty nimi")
    else:
        print("uusi nimi")
        nimet.add(nimi)

print(nimet)