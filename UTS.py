# Program Kalkulator Sederhana

#Input
angka1 = float(input("masukan angka pertama:"))
angka2 = float(input("masukan angka kedua:"))
operator = input("masukan operator(+, -, *, /, **):")

#Proses dan Output
if operator == '+':
    hasil = angka1 + angka2
    keterangan = "tambah"
elif operator == '-':
    hasil = angka1 - angka2
    keterangan = "kurang"
elif operator == '*':
    hasil = angka1 * angka2
    keterangan = "kali"
elif operator == '/':
    hasil = angka1 / angka2
    keterangan = "bagi"
elif operator == '**':
    hasil = angka1 ** angka2
    keterangan = "pangkat"
else:
    print("Operator tidak valid")
    exit()

#Output akhir
print("angka pertama:", angka1)
print("angka kedua:", angka2)
print("pilihan operator:", keterangan)
print(f"hasil operator {angka1} {operator} {angka2} = {hasil}")