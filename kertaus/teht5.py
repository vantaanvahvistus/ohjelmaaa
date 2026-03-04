while True:
    lasku = input("mikä laskutoimitus [+,-,/,*] (lopeta): ")
    if lasku == "+":
        luku1 = float(input("mikä luku "))
        luku2 = float(input("mikä luku "))
        lasku = luku1 + luku2
        print("vastaus = ", lasku)

    if lasku == "-":
        luku1 = float(input("mikä luku "))
        luku2 = float(input("mikä luku "))
        lasku = luku1 - luku2
        print("vastaus = ", lasku)

    if lasku == "/":
        luku1 = float(input("mikä luku "))
        luku2 = float(input("mikä luku "))
        lasku = luku1 / luku2
        print("vastaus = ", lasku)

    if lasku == "*":
        luku1 = float(input("mikä luku "))
        luku2 = float(input("mikä luku "))
        lasku = luku1 * luku2
        print("vastaus = ", lasku)



    elif lasku == "lopeta":
        print("lopetetaan")
        break

