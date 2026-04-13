vuodenajat = ("talvi", "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy")
kuukausi = int(input("anna kuukauden numero (1-12): "))
vastaus = vuodenajat[kuukausi-1]
print(f"kuukauden vuodenaika on {vastaus}")
