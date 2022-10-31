import random


def program():
    while True:
        secimler = ["keçi", "keçi", "araba"]
        kapi1 = kapi2 = kapi3 = 0
        asil = 0

        kapi1 = random.choice(secimler)
        if kapi1 == "keçi":
            del secimler[0]
        else:
            secimler.remove(kapi1)
        kapi2 = random.choice(secimler)
        secimler.remove(kapi2)
        kapi3 = secimler[0]

        while True:
            girdi = int(input("Seçim--> "))
            if girdi > 3 or girdi <= 0:
                print("Geçersiz seçim.")
                continue

            if girdi == 1:
                print(girdi, ". kapı seçildi")
                asil = 1
                if kapi2 == "keçi":
                    print("Kapı 2'de keçi var. Seçiminizi değiştirmek ister misiniz?")
                    degis = input("Seçim--> ")
                    if degis == "e":
                        print("3. kapı seçildi.")
                        asil = 3
                        if kapi3 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break
                    else:
                        print(girdi, "kapısında kaldınız")
                        if kapi1 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break
                elif kapi3 == "keçi":
                    print("Kapı 3'de keçi var. Seçiminizi değiştirmek ister misiniz?")
                    degis = input("Seçim--> ")
                    if degis == "e":
                        print("2. kapı seçildi.")
                        asil = 2
                        if kapi2 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break
                    else:
                        print(girdi, "kapısında kaldınız")
                        if kapi1 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break
            elif girdi == 2:
                asil = 2
                if kapi1 == "keçi":
                    print("Kapı 1'de keçi var. Seçiminizi değiştirmek ister misiniz?")
                    degis = input("Seçim--> ")
                    if degis == "e":
                        print("3. kapı seçildi.")
                        asil = 3
                        if kapi3 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break
                    else:
                        print(girdi, "kapısında kaldınız")
                        if kapi2 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break
                elif kapi3 == "keçi":
                    print("Kapı 3'de keçi var. Seçiminizi değiştirmek ister misiniz?")
                    degis = input("Seçim--> ")
                    if degis == "e":
                        print("1. kapı seçildi.")
                        asil = 1
                        if kapi1 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break
                    else:
                        print(girdi, "kapısında kaldınız")
                        if kapi2 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break
            else:
                if kapi1 == "keçi":
                    print("Kapı 1'de keçi var. Seçiminizi değiştirmek ister misiniz?")
                    degis = input("Seçim--> ")
                    if degis == "e":
                        print("2. kapı seçildi.")
                        asil = 2
                        if kapi2 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break
                    else:
                        print(girdi, "kapısında kaldınız")
                        if kapi3 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break
                elif kapi2 == "keçi":
                    print("Kapı 2'de keçi var. Seçiminizi değiştirmek ister misiniz?")
                    degis = input("Seçim--> ")
                    if degis == "e":
                        print("1. kapı seçildi.")
                        asil = 1
                        if kapi1 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break
                    else:
                        print(girdi, "kapısında kaldınız")
                        if kapi3 == "araba":
                            print("Tebrikler! Kazandınız.")
                            break
                        else:
                            print("Kaybettiniz.")
                            break

program()

