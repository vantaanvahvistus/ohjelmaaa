oppilaat = {
    "paavali":["paavali", 4, "kuvis"],
    "sanna": ["sanna", 9, "ruotsi"],
    "petteri": ["petteri", 1, "käsityö"],
    "sauli": ["sauli", 6, "matikka"]
}
print(f"petterin vuosiluokka: {oppilaat["petteri"][1]}, paavalin lempiaine: {oppilaat["paavali"][2]}")

oppilaat["sanna"][2] = "biologia"
oppilaat["riikka"] = ["riikka", 7, "historia"]
del oppilaat["sauli"]

print(oppilaat)


