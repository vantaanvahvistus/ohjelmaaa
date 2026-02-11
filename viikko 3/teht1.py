import math
pituus = float(input("kuinka pitka kuha on? (cm): "))

if pituus <37:
    print("palauta kuha takaisin veteen")
    print("sallitusta pituudesta puuttuu: ",37 - pituus, "cm")

else:
    print("kuhaa ei tarvitse palauttaa takaisin veteen")


