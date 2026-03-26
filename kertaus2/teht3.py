sanat = ["ruoka", "karkki", "jäätelö", "juoma", "muovi", "auto", "kaali"]

pitkat_sanat = 0
for sana in sanat:
    if len(sana) > 5:
        pitkat_sanat_lkm =+ 1

print(f"listassa on {pitkat_sanat} sanaa jossa oli yli 5 kirjainta")
        