sukupuoli = input("mika on biologinen sukupuoli?: ")
hemoglobiini = float(input("mika on hemoglobiini arvo? (g/l): "))

if sukupuoli == "nainen":
    if 117 <= hemoglobiini < 179:
        print("normaali")
    elif hemoglobiini < 117:
        print("alhainen")
    elif hemoglobiini > 179:
        print("korkea")

elif sukupuoli == "mies":
    if 134 <= hemoglobiini < 195:
        print("normaali")
    elif hemoglobiini < 134:
        print("alhainen")
    elif hemoglobiini > 195:
        print("korkea")
