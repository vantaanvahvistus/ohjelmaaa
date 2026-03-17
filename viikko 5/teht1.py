import random

noppa = int(input("kuinka monta arpakuutiota: "))

summa = 0
for i in range(noppa):
    summa = summa + random.randint(1,6)
print(summa)



