import streamlit as st
import math  # Contoh module yang akan digunakan di halaman Module

# Fungsi contoh untuk halaman Function
def hitung_kuadrat(angka):
    return angka ** 2

# Fungsi contoh lainnya
def sapa(nama):
    return f"Halo, {nama}!"

# Sidebar untuk navigasi halaman
st.sidebar.title("Navigasi Halaman")
page = st.sidebar.radio("Pilih Halaman:", ["If/Match", "Looping", "Function", "Module"])

# Halaman 1: If/Match
if page == "If/Match":
    st.title("Halaman If/Match")
    st.write("Halaman ini mendemonstrasikan penggunaan if/elif/else dan match (pattern matching di Python 3.10+).")
    
    # Input dari user
    pilihan = st.selectbox("Pilih opsi:", ["A", "B", "C"])
    
    # Menggunakan if/elif/else
    if pilihan == "A":
        st.success("Anda memilih A!")
    elif pilihan == "B":
        st.info("Anda memilih B!")
    else:
        st.warning("Anda memilih C!")
    
    # Menggunakan match (jika Python 3.10+)
    st.write("Contoh dengan match:")
    match pilihan:
        case "A":
            st.success("Match: A dipilih!")
        case "B":
            st.info("Match: B dipilih!")
        case "C":
            st.warning("Match: C dipilih!")
        case _:
            st.error("Pilihan tidak valid!")

# Halaman 2: Looping
elif page == "Looping":
    st.title("Halaman Looping")
    st.write("Halaman ini mendemonstrasikan penggunaan looping (for dan while).")
    
    # Input angka untuk looping
    n = st.slider("Pilih angka untuk looping (1-10):", 1, 10, 5)
    
    # For loop
    st.subheader("For Loop: Menampilkan angka dari 1 hingga n")
    for i in range(1, n+1):
        st.write(f"Angka: {i}")
    
    # While loop
    st.subheader("While Loop: Menghitung mundur dari n")
    counter = n
    while counter > 0:
        st.write(f"Hitung mundur: {counter}")
        counter -= 1

# Halaman 3: Function
elif page == "Function":
    st.title("Halaman Function")
    st.write("Halaman ini mendemonstrasikan penggunaan function (fungsi).")
    
    # Input untuk function
    angka = st.number_input("Masukkan angka untuk dihitung kuadrat:", value=5)
    nama = st.text_input("Masukkan nama untuk disapa:", value="Pengguna")
    
    # Panggil function
    hasil_kuadrat = hitung_kuadrat(angka)
    salam = sapa(nama)
    
    st.success(f"Kuadrat dari {angka} adalah {hasil_kuadrat}")
    st.info(salam)
    
    # Function dengan return multiple values
    def hitung_luas_dan_keliling(persegi_panjang):
        panjang, lebar = persegi_panjang
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        return luas, keliling
    
    panjang = st.number_input("Panjang:", value=10)
    lebar = st.number_input("Lebar:", value=5)
    luas, keliling = hitung_luas_dan_keliling((panjang, lebar))
    st.write(f"Luas: {luas}, Keliling: {keliling}")

# Halaman 4: Module
elif page == "Module":
    st.title("Halaman Module")
    st.write("Halaman ini mendemonstrasikan penggunaan module (import modul).")
    
    # Menggunakan modul math
    st.subheader("Menggunakan modul math")
    angka = st.number_input("Masukkan angka untuk sqrt dan sin:", value=4.0)
    sqrt_hasil = math.sqrt(angka)
    sin_hasil = math.sin(math.radians(angka))  # Konversi ke radian
    
    st.write(f"Akar kuadrat dari {angka} adalah {sqrt_hasil}")
    st.write(f"Sin dari {angka} derajat adalah {sin_hasil}")
    
    # Menggunakan modul random (import di atas jika perlu, tapi untuk contoh)
    import random
    st.subheader("Menggunakan modul random")
    if st.button("Generate angka acak"):
        acak = random.randint(1, 100)
        st.success(f"Angka acak: {acak}")
    
    # Contoh import custom (misal, tapi di sini pakai built-in)
    st.write("Modul memungkinkan kita menggunakan kode dari file lain atau library eksternal.")