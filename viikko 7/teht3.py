lentoasemat = {}

while True:
    valinta = input("valitse haluamasi toiminto. 1 = syötä uusi asema, 2 = aseman tiedot (tyhjä lopettaa): ")
    if valinta == "1":
        icao = input("anna aseman icao-koodi: ")
        nimi = input("anna aseman nimi: ")
        lentoasemat[icao] = nimi
        print("asema tallennettu")

    elif valinta == "2":
        icao = input("anna aseman icao-koodi: ")
        if icao in lentoasemat:
            print(f"icao-koodin {icao} asema on: {lentoasemat[icao]} ")
        else:
            print("koodilla ei asemaa")
    elif valinta == "":
        print("lopetetaan")
        break