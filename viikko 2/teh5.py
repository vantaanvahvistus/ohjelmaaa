import math
leiviskat = int(input("anna leiviskat: "))
naulat = int(input("anna naulat: "))
luodit = int(input("anna luodit: "))

luoti_grammoina = 13.3
naulat_luoteina = 32
leiviskat_nauloina = 20

yhteensa_luodit = ( leiviskat * leiviskat_nauloina * naulat_luoteina ) + ( (naulat * naulat_luoteina) + luodit )
grammat_yhteensa = (yhteensa_luodit * luoti_grammoina)

kilogrammat = int(grammat_yhteensa) // 1000
grammat = int(grammat_yhteensa) % 1000

print(f"massa nykymittojen mukaan: ")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa")
