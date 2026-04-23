nimet = {
        "john":["john", 30, "engineer"],
        "emily": ["emily", 25, "artist"],
        "anna": ["anna", 22, "student"]
}

print(f"nimi:{nimet['john'][0]}, ikä:{nimet['john'][1]}, emilyn ammatti:{nimet['emily'][2]}")


nimet["anna"][2] = "teacher"
nimet["james"] = ["james", 28, "writer"]

nimet["sophia"] = ["sophia", 35, "doctor"]

del nimet ["emily"]

print(nimet)

