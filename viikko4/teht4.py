import random

luku = random.randint(1,10)

arvaus = int(input("syötä luku: "))

while True:
    if arvaus == luku:
        print("oikein")
        break

    if arvaus < luku:
        print("liian pieni")
        arvaus = int(input("syötä luku: "))

    if arvaus > luku:
        print("liian suuri")
        arvaus = int(input("syötä luku: "))