def summa(a, b):
    return a + b
def erotus(a, b):
    return a - b
def jako(a, b):
    if b == 0:
        return "ei voi jakaa nollalla"
    return a / b
def kerto(a, b):
    return a * b

while True:
    lasku = input("mikä laskutoimitus [+,-,/,*,lopeta]: ")
    if lasku == "lopeta":
        print("lopetetaan")
        break
    luku1 = float(input("mikä luku "))
    luku2 = float(input("mikä luku "))

    if lasku == "+":
        vastaus = summa(luku1, luku2)
    elif lasku == "-":
        vastaus = erotus(luku1, luku2)
    elif lasku == "/":
        vastaus = jako(luku1, luku2)
    elif lasku == "*":
        vastaus = kerto(luku1, luku2)

    print(f"vastaus = {vastaus}")




