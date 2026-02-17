import streamlit as st
import random  # Modul untuk menghasilkan ID unik atau elemen acak
import datetime  # Modul untuk tanggal dan waktu
import json  # Modul untuk menyimpan dan memuat data CV

# ReportLab 
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import ImageReader
    REPORTLAB_AVAILABLE = True
except Exception:
    REPORTLAB_AVAILABLE = False

# Fungsi untuk menyimpan data CV ke file JSON
def save_cv_data(data):
    with open("cv_data.json", "w") as f:
        json.dump(data, f)

# Fungsi untuk memuat data CV dari file JSON
def load_cv_data():
    try:
        with open("cv_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Fungsi untuk halaman Beranda
def home_page():
    st.title("Selamat Datang di CV Maker for Engineers")
    st.image("https://enhancv-cms-screenshots.s3.amazonaws.com/resumes-meta-images/design-engineer-lOKiugT9W9afZySwztKNsqhUlaqJwwzI5uVPv3Re.png", width="stretch")
    st.write("Buat CV profesional untuk insinyur dengan mudah. Isi data Anda dan lihat preview CV.")
    
    # Menggunakan if-else untuk menampilkan pesan berdasarkan waktu
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        st.write("Selamat pagi! Mulai buat CV Anda hari ini.")
    elif current_hour < 18:
        st.write("Selamat siang! Waktunya update CV.")
    else:
        st.write("Selamat malam! Kami siap membantu buatkan CV untuk kesuksesan karir anda kedepannya.")

# Fungsi untuk halaman Buat CV
def create_cv_page():
    st.title("Buat CV Anda")
    st.write("Isi informasi pribadi dan pengalaman Anda.")
    
    # Form untuk input data
    with st.form("cv_form"):
        name = st.text_input("Nama Lengkap")
        email = st.text_input("Email")
        phone = st.text_input("Nomor Telepon")
        address = st.text_input("Alamat")
        birth_date = st.date_input("Tanggal Lahir")
        
        # Menggunakan looping untuk input pengalaman kerja
        st.subheader("Pengalaman Kerja")
        experiences = []
        num_experiences = st.number_input("Jumlah Pengalaman Kerja", min_value=0, max_value=5, value=1)
        for i in range(num_experiences):  # Looping
            job_title = st.text_input(f"Jabatan {i+1}")
            company = st.text_input(f"Perusahaan {i+1}")
            duration = st.text_input(f"Durasi {i+1} (contoh, 2020-2023)")
            experiences.append({"job_title": job_title, "company": company, "duration": duration})
        
        # Menggunakan looping untuk input pendidikan
        st.subheader("Pendidikan")
        educations = []
        num_educations = st.number_input("Jumlah Pendidikan", min_value=0, max_value=3, value=1)
        for i in range(num_educations):  # Looping
            degree = st.text_input(f"Gelar {i+1}")
            institution = st.text_input(f"Institusi {i+1}")
            year = st.text_input(f"Tahun {i+1}")
            educations.append({"degree": degree, "institution": institution, "year": year})
        
        submitted = st.form_submit_button("Simpan CV")
        if submitted:  # If-else untuk validasi
            if name and email:
                cv_id = random.randint(1000, 9999)  # Modul random untuk ID unik
                cv_data = {
                    "id": cv_id,
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "address": address,
                    "birth_date": str(birth_date),
                    "experiences": experiences,
                    "educations": educations
                }
                all_data = load_cv_data()
                all_data[str(cv_id)] = cv_data
                save_cv_data(all_data)
                st.success(f"CV berhasil disimpan dengan ID: {cv_id}")
            else:
                st.error("Harap isi nama dan email.")

# Fungsi untuk halaman Lihat CV
def view_cv_page():
    st.title("Lihat CV Anda")
    st.write("Masukkan ID CV untuk melihat preview.")
    
    cv_id = st.text_input("ID CV")
    if st.button("Lihat CV"):
        all_data = load_cv_data()
        if cv_id in all_data:  # If-else untuk cek data
            cv = all_data[cv_id]
            st.subheader(f"CV {cv['name']}")
            st.write(f"Email: {cv['email']}")
            st.write(f"Telepon: {cv['phone']}")
            st.write(f"Alamat: {cv['address']}")
            st.write(f"Tanggal Lahir: {cv['birth_date']}")
            
            st.subheader("Pengalaman Kerja")
            for exp in cv["experiences"]:  # Looping untuk tampilkan pengalaman
                st.write(f"- {exp['job_title']} di {exp['company']} ({exp['duration']})")
            
            st.subheader("Pendidikan")
            for edu in cv["educations"]:  # Looping untuk tampilkan pendidikan
                st.write(f"- {edu['degree']} dari {edu['institution']} ({edu['year']})")
        else:
            st.error("ID CV tidak ditemukan.")
            

# Fungsi untuk halaman Tentang
def about_page():
    st.title("Tentang CV Maker")
    st.write("Aplikasi ini membantu insinyur membuat CV profesional dengan mudah.")
    st.write("Dibuat menggunakan Streamlit, dengan fitur input data, preview, dan penyimpanan.")
    
    # Menggunakan looping untuk menampilkan fitur
    features = ["Input data pribadi", "Tambah pengalaman kerja", "Tambah pendidikan", "Preview CV", "Simpan dan muat data"]
    st.subheader("Fitur Utama")
    for feature in features:  # Looping
        st.write(f"- {feature}")

# Sidebar untuk navigasi
st.sidebar.title("Navigasi CV Maker")
page = st.sidebar.radio("Pilih Halaman", ["Beranda", "Buat CV", "Lihat CV", "Tentang"])

# Menggunakan if-else untuk menampilkan halaman berdasarkan pilihan
if page == "Beranda":
    home_page()
elif page == "Buat CV":
    create_cv_page()
elif page == "Lihat CV":
    view_cv_page()
elif page == "Tentang":
    about_page()
else:
    st.error("Halaman tidak ditemukan.")