# soal nomor 1

bilangan = int(input("masukan nilai"))

if bilangan % 2 == 0:
    print("bilangan genap")
else: 
    print("bilangan ganjil")

# soal nomor 2

nilai = int(input("masukan nilai"))
if nilai >75:
    print("LULUS")
else : 
    print ("MAAF ANDA TIDAK LULUS")

# nomor 3

usia = int(input("masukan usia anda : "))
if usia >= 18:
    print("Dewasa")
elif usia > 13 and usia <17:
    print("remaja")
else :
    print("anak anak")

# nomor 4

warna = (input("masukan warna favorit anda"))
if warna == "gold" or warna == "silver" :
    print("selamat anda mendapatkan diskon")
else :
    print("mohon maaf anda tidak mendapatkan diskon")

# nomor 5

jumlah_beli = int(input("masukan jumlah pembelian anda"))
print("selamat anda mendapatkan diskon 10%") if jumlah_beli > 100 else print("mohon maaf anda tidak mendapatkan diskon")