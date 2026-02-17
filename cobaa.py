import streamlit as st

# Fungsi untuk halaman Beranda
def home_page():
    st.title("Selamat Datang di Pet Shop Kami")
    st.image("https://via.placeholder.com/800x400?text=Pet+Shop+Hero", use_column_width=True)
    st.write("Rumah untuk hewan peliharaan Anda. Temukan hewan peliharaan dan aksesoris terbaik.")
    st.subheader("Produk Unggulan")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://via.placeholder.com/200x200?text=Anjing+Ras", caption="Anjing Ras - Rp 500.000")
    with col2:
        st.image("https://via.placeholder.com/200x200?text=Kucing", caption="Kucing - Rp 300.000")
    with col3:
        st.image("https://via.placeholder.com/200x200?text=Aksesoris", caption="Aksesoris - Rp 50.000")

# Fungsi untuk halaman Produk
def products_page():
    st.title("Produk Kami")
    st.write("Jelajahi berbagai produk hewan peliharaan kami.")
    products = [
        {"name": "Anjing Ras", "price": "Rp 500.000", "desc": "Berbagai ras anjing sehat."},
        {"name": "Kucing", "price": "Rp 300.000", "desc": "Kucing lucu dan energik."},
        {"name": "Aksesoris", "price": "Rp 50.000", "desc": "Kandang, mainan, dan makanan."},
        {"name": "Burung", "price": "Rp 200.000", "desc": "Burung peliharaan yang indah."}
    ]
    for product in products:
        st.subheader(product["name"])
        st.write(f"Harga: {product['price']}")
        st.write(product["desc"])
        st.button(f"Beli {product['name']}", key=product["name"])

# Fungsi untuk halaman Tentang Kami
def about_page():
    st.title("Tentang Kami")
    st.write("Kami adalah pet shop terpercaya yang menyediakan berbagai jenis hewan peliharaan, makanan, dan aksesoris dengan harga terjangkau.")
    st.write("Komitmen kami adalah memberikan pelayanan terbaik untuk Anda dan hewan peliharaan Anda.")
    st.subheader("Tim Kami")
    st.write("- Pemilik: John Doe")
    st.write("- Staf: Jane Smith, dll.")

# Fungsi untuk halaman Kontak
def contact_page():
    st.title("Kontak Kami")
    st.write("Hubungi kami untuk informasi lebih lanjut.")
    st.write("Alamat: Jl. Pet Shop No. 123, Kota Anda")
    st.write("Telepon: (021) 123-4567")
    st.write("Email: info@petshop.com")
    with st.form("contact_form"):
        name = st.text_input("Nama Anda")
        email = st.text_input("Email")
        message = st.text_area("Pesan")
        submitted = st.form_submit_button("Kirim")
        if submitted:
            st.success("Pesan Anda telah dikirim!")

# Sidebar untuk navigasi
st.sidebar.title("Navigasi Pet Shop")
page = st.sidebar.radio("Pilih Halaman", ["Beranda", "Produk", "Tentang Kami", "Kontak"])

# Menampilkan halaman berdasarkan pilihan
if page == "Beranda":
    home_page()
elif page == "Produk":
    products_page()
elif page == "Tentang Kami":
    about_page()
elif page == "Kontak":
    contact_page()