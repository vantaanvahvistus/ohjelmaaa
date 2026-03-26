def kuusi(koko):
    print("tämä on kuusi")
    print(" " * 15)

    for i in range(1, koko + 1):
        tahdet = 2 * i - 1
        valilyonnit = koko - i

        print(" " * valilyonnit + "*" * tahdet + "\n", end="")

    print(" " * (koko - 1) + "*" + "\n", end="")

kuusi(10)
