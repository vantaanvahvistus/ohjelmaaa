kayttajatunnus = "python"
salasana = "rules"

yritykset = 0
maksimi = 5

while yritykset < maksimi:
    tunnus = input(" anna käyttäjätunnus:")
    sala = input(" anna salasana:")

    if tunnus == kayttajatunnus and sala == salasana:
        print("tervetuloa")
        break
    else:
        yritykset = yritykset + 1

        if yritykset < maksimi:
            print("väärin")

if yritykset == maksimi:
    print("pääsy evätty")

