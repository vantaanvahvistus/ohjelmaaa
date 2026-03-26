import math

luku = int(input("anna luku väliltä 1-10: "))

if 1 <= luku <= 10:
    print(f"luvun {luku} kertotaulu")
    print("" * 15)

for i in range(1, 11):
    tulos = i * luku
    print(f"{i:2} * {luku} = {tulos}")
    