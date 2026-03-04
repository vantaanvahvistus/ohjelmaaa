tuntipalkka = float(input("mikä on tuntipalkka: "))
tunnit = float(input("mitkä on tehdyt tunnit: "))
viikonpaiva = input("mikä on viikonpaiva: ")
tupla = "sunnuntai"

palkka = tuntipalkka * tunnit
if viikonpaiva == "sunnuntai":
    palkka2 = 2 * palkka
    print("päiväpalkka =", palkka2)
else:
    print("päiväpalkka =", palkka)

