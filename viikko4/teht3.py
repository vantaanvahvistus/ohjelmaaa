kasky = input("anna luku, tyhjä lopettaa: ")
luku = float(kasky)
pienin = luku
suurin = luku

while True:
    kasky = input("anna luku, tyhjä lopettaa: ")
    if kasky == "":
        break

    luku = float(kasky)

    if luku < pienin:
        pienin = luku

    if luku > suurin:
        suurin = luku

print(f"Pienin luku: {pienin}")
print(f"Suurin luku: {suurin}")