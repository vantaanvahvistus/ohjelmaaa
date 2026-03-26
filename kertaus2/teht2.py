luvut = []
while True:
    syote = int(input("uusi arvo: "))

    if syote == 0:
     print("loppu")
    break

luvut.append(syote)
print(f"lista nyt: {luvut}")
print(f"lista järjestyksessä: {sorted(luvut)}")

