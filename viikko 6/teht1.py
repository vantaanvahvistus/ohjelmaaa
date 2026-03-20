import random

def heitto():
    tulos = random.randint(1, 6)
    return tulos


#pääohjelma

print("heitä noppaa kunnes saat arvon kuusi")
luku = 0
while luku != 6:
    luku = heitto()
    print(f"sait{luku}")
    