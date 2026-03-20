def laske_summa(lista):
    kokonaissumma = 0

    for luku in lista:
        kokonaissumma = kokonaissumma + luku

    return kokonaissumma

#pääohjelma

_luvut = [7, 4, 6, 1]
tulos = laske_summa(_luvut)

print(f"lukujen summa on: {tulos}")