vuosiluku = float(input("mika vuosiluku?: "))

if vuosiluku % 4 == 0:
    print("karkausvuosi ")

elif vuosiluku % 100 == 0:
    if vuosiluku % 400 == 0:
        print("karkausvuosi ")
    else:
        print("ei karkausvuosi ")

else:
    print("ei karkausvuosi ")

