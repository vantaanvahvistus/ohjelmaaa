lentoasemat = {}

while True:
    print("valitse haluamasi toiminto")
    print("1, syötä uusi lentoasema: ")
    print("2, lentoaseman tiedot: ")
    print("3, lopeta: ")

    valinta = input("valitsit: ")
    if valinta == "1":
        icao = input("anna aseman icao-koodi: ")
        nimi = input("anna aseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"asema {icao} tallennettu")

    elif valinta == "2":
        icao = input("anna aseman icao-koodi: ")
        if icao in lentoasemat:
            print(f"icao-koodin {icao} asema on: {lentoasemat[icao]} ")
        else:
            print("koodilla {icao} ei löytynyt sopivaa asemaa")
    elif valinta == "3":
        print("ohjelma päättyy")
        break

