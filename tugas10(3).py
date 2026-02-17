import modul_bangun_ruang as br # type: ignore
import modul_bangun_datar as bd # type: ignore

print("~~ BANGUN RUANG~~ ")
print(f"Volum Kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"Volum balok adalah {br.balok(4, 5, 2)}")
print(f"Volum Prisma Segitiga adalah {br.prisma(5,4,5)}")
print(f"Volum Tabung dengan jari-jari 7 dan tinggi 10 adalah {br.tabung(7, 10)}")
print(f"Volum Kerucut dengan jari-jari 5 dan tinggi 12 adalah {br.kerucut(5, 12)}")

print(" ~~BANGUN DATAR ~~")
print(f"Luas Persegi dengan sisi 4 adalah {bd.persegi(4)}")
print(f"Luas Persegi Panjang dengan panjang 6 dan lebar 8 adalah {bd.persegi_panjang(6, 8)}")
print(f"Luas Segitiga dengan alas 10 dan tinggi 5 adalah {bd.segitiga(10, 5)}")
print(f"Luas Lingkaran dengan jari-jari 7 adalah {bd.lingkaran(7)}")
print(f"Luas JajarGenjang dengan alas 9 dan tinggi 4 adalah {bd.jajargenjang(9, 4)}")