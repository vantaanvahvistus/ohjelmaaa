hytti = input("kerro laivan hyttiluokka ")

if hytti == "lux":
    print("parvekkeellinen hytti ylakannalla")
elif hytti == "A":
    print("ikkunallinen hytti autokannen ylapuolella")
elif hytti == "B":
    print("ikkunaton hytti autokannen ylapuolella")
elif hytti == "C":
    print("ikkunaton hytti autokannen alapuolella")
else:
    print("virheellinen hyttiluokka")