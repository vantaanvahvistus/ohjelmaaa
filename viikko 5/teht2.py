luvut = []

while True:
    numero = input("anna luku: ")
    if numero == "":
        break
    luku = int(numero)
    luvut.append(luku)

luvut.sort(reverse=True)
print("viisi suurinta lukua ovat: ")
for luku in luvut[0:5]:
    print(luku)

