import streamlit as st

# Halaman 1: Judul
def halaman_judul():
    st.title("Maker CV Engineer")
    st.write("Selamat datang di Maker CV Engineer!")
    st.write("Isi informasi Anda di halaman berikutnya.")

# Halaman 2: Informasi Pribadi
def halaman_informasi():
    st.header("Informasi Pribadi")
    nama = st.text_input("Nama")
    email = st.text_input("Email")
    telepon = st.text_input("Nomor Telepon")
    return nama, email, telepon

# Halaman 3: Pengalaman Kerja
def halaman_pengalaman(nama):
    st.header("Pengalaman Kerja")
    pekerjaan = st.text_input("Jabatan Terakhir")
    perusahaan = st.text_input("Nama Perusahaan")
    tahun_mulai = st.text_input("Tahun Mulai")
    tahun_selesai = st.text_input("Tahun Selesai")
    st.write(f"CV untuk {nama} telah dibuat!")
    return pekerjaan, perusahaan, tahun_mulai, tahun_selesai

# Halaman 4: Download CV
def halaman_download(nama, email, telepon, pekerjaan, perusahaan, tahun_mulai, tahun_selesai):
    st.header("Download CV")
    st.write("Berikut adalah informasi CV Anda:")
    st.write(f"**Nama:** {nama}")
    st.write(f"**Email:** {email}")
    st.write(f"**Telepon:** {telepon}")
    st.write(f"**Jabatan:** {pekerjaan} di {perusahaan} ({tahun_mulai} - {tahun_selesai})")
    
    # Tombol untuk mendownload CV
    if st.button("Download CV"):
        st.success("CV berhasil di-download!")

# Menyusun struktur aplikasi
def main():
    st.sidebar.title("Navigasi")
    pilihan = st.sidebar.radio("Pilih Halaman", ["Judul", "Informasi Pribadi", "Pengalaman Kerja", "Download CV"])

    if pilihan == "Judul":
        halaman_judul()
    elif pilihan == "Informasi Pribadi":
        nama, email, telepon = halaman_informasi()
        if st.button("Lanjut ke Pengalaman Kerja"):
            st.session_state.nama = nama
            st.session_state.email = email
            st.session_state.telepon = telepon
    elif pilihan == "Pengalaman Kerja":
        if 'nama' in st.session_state:
            pekerjaan, perusahaan, tahun_mulai, tahun_selesai = halaman_pengalaman(st.session_state.nama)
            if st.button("Lanjut ke Download CV"):
                st.session_state.pekerjaan = pekerjaan
                st.session_state.perusahaan = perusahaan
                st.session_state.tahun_mulai = tahun_mulai
                st.session_state.tahun_selesai = tahun_selesai
        else:
            st.warning("Silakan isi informasi pribadi terlebih dahulu.")
    elif pilihan == "Download CV":
        if all(k in st.session_state for k in ['nama', 'email', 'telepon', 'pekerjaan', 'perusahaan', 'tahun_mulai', 'tahun_selesai']):
            halaman_download(st.session_state.nama, st.session_state.email, st.session_state.telepon,
                             st.session_state.pekerjaan, st.session_state.perusahaan,
                             st.session_state.tahun_mulai, st.session_state.tahun_selesai)
        else:
            st.warning("Silakan isi informasi di halaman sebelumnya.")

if __name__ == "__main__":
    main()
