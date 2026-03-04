from math import sqrt

luku = int(input("anna kokonaisluku: "))
while luku != 0:
    if luku > 0:
        neliojuuri = sqrt(luku)
        print(neliojuuri)
    else:
        print("virheellinen luku")

    luku = int(input("anna kokonaisluku: "))

print("suljetaan...")