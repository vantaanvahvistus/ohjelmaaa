kerroin = 2.54

while True:
    tuumat = float(input("anna tuumat: "))
    if tuumat < 0:
        print("ohjelma loppuu...")
        break

    senttimetrit = tuumat * kerroin
    print(f"{tuumat} tuumaa on {senttimetrit} cm.")

