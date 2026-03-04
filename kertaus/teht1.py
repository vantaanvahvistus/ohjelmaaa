nimi = "matti"
sari = (input("mikä on nimesi? "))

if sari == nimi:
    print("seuraava, kiitos! ")
else:
    annos = float(input("montako keittoannosta? "))
    hinta = 5.90 * annos
    print("kokonaishinta on ", hinta)
    print("seuraava, kiitos! ")
