import streamlit as st
from io import BytesIO
import json
from PIL import Image

# ReportLab 
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import ImageReader
    REPORTLAB_AVAILABLE = True
except Exception:
    REPORTLAB_AVAILABLE = False

st.set_page_config(page_title="CV Builder - Streamlit", layout="wide")

st.title("CV Builder — Streamlit")
st.write("Isi formulir di kolom kiri, lihat preview di kanan, lalu unduh CV-mu.")

# =========================
# SESSION STATE
# =========================
if "edu_count" not in st.session_state:
    st.session_state.edu_count = 1
if "exp_count" not in st.session_state:
    st.session_state.exp_count = 1

col1, col2 = st.columns([1, 1])

# =========================
# FORM KIRI
# =========================
with col1:
    st.header("Formulir CV")

    name = st.text_input("Nama lengkap", "Muhammad Hilmi")
    title = st.text_input("Posisi / Judul singkat", "Frontend Developer")
    contact = st.text_input(
        "Kontak (email • telepon • lokasi)",
        "hilmi@example.com • +62 812 3456 7890 • Jakarta"
    )

    # FOTO PROFIL
    st.markdown("---")
    st.subheader("Foto Profil")
    photo = st.file_uploader(
        "Upload foto (JPG / PNG)",
        type=["jpg", "jpeg", "png"]
    )

    summary = st.text_area(
        "Ringkasan singkat (1-3 kalimat)",
        "Profesional web developer dengan pengalaman 3 tahun membangun aplikasi front-end yang responsif dan cepat."
    )

    # =========================
    # PENDIDIKAN
    # =========================
    st.markdown("---")
    st.subheader("Pendidikan")

    for i in range(st.session_state.edu_count):
        st.text_input(
            f"Pendidikan #{i+1} - Gelar / Jurusan",
            key=f"edu_title_{i}",
            value="S1 Teknik Informatika"
        )
        st.text_input(
            f"Pendidikan #{i+1} - Institusi & Tahun",
            key=f"edu_sub_{i}",
            value="Universitas Contoh • 2017 - 2021"
        )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Tambah Pendidikan"):
            st.session_state.edu_count += 1
    with c2:
        if st.session_state.edu_count > 1 and st.button("Hapus Pendidikan"):
            st.session_state.edu_count -= 1

    # =========================
    # PENGALAMAN
    # =========================
    st.markdown("---")
    st.subheader("Pengalaman Kerja")

    for i in range(st.session_state.exp_count):
        st.text_input(
            f"Pengalaman #{i+1} - Jabatan",
            key=f"exp_title_{i}",
            value="Frontend Developer"
        )
        st.text_area(
            f"Pengalaman #{i+1} - Deskripsi",
            key=f"exp_sub_{i}",
            value="Membangun antarmuka pengguna, optimasi performa."
        )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Tambah Pengalaman"):
            st.session_state.exp_count += 1
    with c2:
        if st.session_state.exp_count > 1 and st.button("Hapus Pengalaman"):
            st.session_state.exp_count -= 1

    # =========================
    # SKILL & SERTIFIKAT
    # =========================
    st.markdown("---")
    skills = st.text_input("Keahlian (pisahkan dengan koma)", "HTML, CSS, JavaScript, React")
    certs = st.text_area("Sertifikat / Pelatihan (opsional, tiap baris satu)", "")

    st.markdown("---")
    if st.checkbox("Tampilkan tanggal pembuatan pada CV", True):
        import datetime
        created_date = datetime.date.today().strftime("%d %B %Y")
    else:
        created_date = None

    # =========================
    # KUMPULKAN DATA
    # =========================
    def gather_data():
        data = {
            "name": name,
            "title": title,
            "contact": contact,
            "summary": summary,
            "photo": photo,
            "educations": [],
            "experiences": [],
            "skills": [s.strip() for s in skills.split(",") if s.strip()],
            "certificates": [c.strip() for c in certs.split("\n") if c.strip()],
            "created_date": created_date
        }

        for i in range(st.session_state.edu_count):
            t = st.session_state.get(f"edu_title_{i}", "")
            s = st.session_state.get(f"edu_sub_{i}", "")
            if t or s:
                data["educations"].append({"title": t, "detail": s})

        for i in range(st.session_state.exp_count):
            t = st.session_state.get(f"exp_title_{i}", "")
            s = st.session_state.get(f"exp_sub_{i}", "")
            if t or s:
                data["experiences"].append({"title": t, "detail": s})

        return data

    data = gather_data()

    # =========================
    # PDF EXPORT (FIX)
    # =========================
    def wrap_text(text, max_chars):
        words = text.split()
        lines, cur = [], ""
        for w in words:
            if len(cur) + len(w) + 1 <= max_chars:
                cur += " " + w if cur else w
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def create_pdf_bytes(data):
        buffer = BytesIO()

        if not REPORTLAB_AVAILABLE:
            buffer.write(json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8"))
            buffer.seek(0)
            return buffer

        c = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4
        margin = 50
        y = height - margin

        # FOTO PROFIL PDF (FIX ImageReader)
        if data.get("photo"):
            try:
                img = Image.open(data["photo"]).convert("RGB")
                img.thumbnail((80, 80))
                img_reader = ImageReader(img)
                c.drawImage(img_reader, width - margin - 80, y - 80, 80, 80, mask="auto")
            except Exception:
                pass

        c.setFont("Helvetica-Bold", 18)
        c.drawString(margin, y, data["name"])
        c.setFont("Helvetica", 12)
        c.drawString(margin, y - 22, data["title"])
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(margin, y - 40, data["contact"])
        y -= 80

        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, y, "Ringkasan")
        y -= 16
        c.setFont("Helvetica", 10)
        for line in wrap_text(data["summary"], 90):
            c.drawString(margin, y, line)
            y -= 12

        c.save()
        buffer.seek(0)
        return buffer

    st.markdown("---")
    col_pdf, col_json, col_txt = st.columns(3)

    with col_pdf:
        if REPORTLAB_AVAILABLE:
            st.download_button(
                "Download PDF",
                data=create_pdf_bytes(data),
                file_name=f"{name}.pdf",
                mime="application/pdf"
            )

    with col_json:
        st.download_button(
            "Download JSON",
            data=json.dumps(data, ensure_ascii=False, indent=2),
            file_name=f"{name}.json"
        )

    with col_txt:
        txt_data = json.dumps(data, ensure_ascii=False, indent=2)
        st.download_button(
            "Download TXT",
            data=txt_data,
            file_name=f"{name}.txt"
        )

# =========================
# PREVIEW KANAN
# =========================
with col2:
    st.header("Preview CV")

    if data.get("photo"):
        st.image(Image.open(data["photo"]), width=150)

    st.subheader(name)
    st.write(f"**{title}**")
    st.write(contact)
    st.markdown("---")
    st.write("**Ringkasan**")
    st.write(summary)
    st.markdown("---")
    st.write("**Pendidikan**")
    for edu in data["educations"]:
        st.markdown(f"**{edu['title']}**  \n{edu['detail']}")
    st.markdown("---")
    st.write("**Pengalaman Kerja**")
    for exp in data["experiences"]:
        st.markdown(f"**{exp['title']}**  \n{exp['detail']}")
    st.markdown("---")
    st.write("**Keahlian**")
    st.write(", ".join(data["skills"]))