
def muunnos(galloonat):
    litrat = galloonat * 3.785
    return litrat

#pääojelma

while True:
    m_galloona = float(input("anna galloonamäärä, negatiivinen lopettaa"))
    if m_galloona < 0:
        print("ohjelma loppuu")
        break

    tulos = muunnos(m_galloona)
    print(f"{m_galloona} galloonaa litroina on {tulos}:")
