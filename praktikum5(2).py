nilai = int(input("""Silahkan pilih menu yang diinginkan
                1. luas persegi
                2. luas lingkaran
                3. luas segitiga
                """))

match nilai:
    case 1:
        sisi = int(input("masukan sisi "))
        total = sisi * sisi

        print("luas persegi adalah ",total)
        #luas persegi
    case "2":
        jari = int(input("masukan jari-jari "))
        total = 3.14*jari*jari

        print("luas lingkaran adalah ",total)
        #luas lingkaran
        #phi * jarijari**2
    case "3":
        alas = int(input("masukan alas "))
        tinggi = int(input("masukan tinggi "))
        total = alas*tinggi/2
        print("luas segitiga adalah ",total)

        # luas segitiga
        # (alas * tinggi)/2 1
    case _:
        print("sampai nanti lagii...hahahahaha...")