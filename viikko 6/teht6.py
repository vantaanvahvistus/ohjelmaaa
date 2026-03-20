import math

def laske_yksikkohinta(halkaisija_cm, hinta_euroa):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala = math.pi * (sade_m ** 2)
    yksikkohinta = hinta_euroa / pinta_ala
    return yksikkohinta

#pääohjelma

print("pizza1 ominaisuudet: ")
h1 = float(input("halkaisija (cm): "))
p1 = float(input("pinta (euroa): "))

print("pizza2 ominaisuudet: ")
h2 = float(input("halkaisija (cm): "))
p2 = float(input("pinta (euroa): "))

hinta1 = laske_yksikkohinta(h1, p1)
hinta2 = laske_yksikkohinta(h2, p2)

print(f"pizza1 maksaa {hinta1}")
print(f"pizza2 maksaa {hinta2}")

if hinta1 < hinta2:
    print("pizza1 on parempi vaihtoehto rahalle")
elif hinta2 < hinta1:
    print("pizza2 on parempi vaihto rahalle")
else:
    print("molemmat pizzat ovat samanarvoisia")


