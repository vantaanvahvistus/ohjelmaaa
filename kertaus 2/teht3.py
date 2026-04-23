kirjasto = {
    "keittokirja": ["sofi oksanen", 1993, "tietokirja"],
    "tuntematon sotilas": ["väino linna", 1956, "romaani"],
    "pipsa possu": ["chris brown", 2003, "lastenkirja"],
    "maailman sodat": ["nikolai oli", 2024, "historiakirja"]
}

print(f"kirjoittaja: {kirjasto["maailman sodat"][0]}, genre: {kirjasto["keittokirja"][2]}")

kirjasto["pipsa possu"][2] = "novelli"
kirjasto["hevoskirja"] = ["mari perankoski", 2017, "tietokirja"]
del kirjasto["tuntematon sotilas"]

print(kirjasto)
