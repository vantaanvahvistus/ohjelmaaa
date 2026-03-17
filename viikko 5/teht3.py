luku = int(input("anna kokonaisluku: "))

on = True

if luku <= 1:
    on = False
else:
    for i in range(2, luku):
        if luku % i == 0:
            on = False
            break

if on:
    print(f"{luku} on alkuluku")
else:
    print(f"{luku} ei ole alkuluku")
