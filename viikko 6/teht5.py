def karsi_parittomat(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0: uusi_lista.append(luku)

    return uusi_lista

#pääohjelma

alkuperaiset = [7, 4, 6, 1]
karsittu = karsi_parittomat(alkuperaiset)
print(f"alkuperäinen: {alkuperaiset}")
print(f"karsittu: {karsittu}")

