import random

def heitto(sivut):
    tulos = random.randint(1, sivut)
    return tulos


#pääohjelma
maks = int(input("kuinka monta sivua nopassa on"))
print("heitä noppaa")
luku = 0
while luku != maks:
    luku = heitto(maks)
    print(f"sait{luku}")