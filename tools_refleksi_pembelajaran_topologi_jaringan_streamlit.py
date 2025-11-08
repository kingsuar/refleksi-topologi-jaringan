import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Refleksi Pembelajaran Topologi Jaringan", layout="wide")

st.title("🧠 Refleksi & Kuis Pembelajaran Topologi Jaringan")

st.markdown("""
Selamat datang di **alat refleksi pembelajaran topologi jaringan**.  
Silakan isi data diri, jawab 5 pertanyaan pilihan ganda,  
dan berikan saran pembelajaran di bagian akhir.
""")

# Bagian Identitas
st.subheader("🪪 Identitas Siswa")
col1, col2, col3 = st.columns(3)
with col1:
    nama = st.text_input("Nama Lengkap")
with col2:
    kelas = st.text_input("Kelas (misal: XI A,B,C)")
with col3:
    absen = st.text_input("No. Absen")

# Daftar pertanyaan kuis
questions = [
    {
        "q": "1️⃣ Apa pengertian dari topologi jaringan?",
        "options": [
            "A. Struktur fisik dan logis bagaimana perangkat saling terhubung",
            "B. Jenis kabel yang digunakan dalam jaringan",
            "C. Proses mengirim data dari satu komputer ke komputer lain",
            "D. Protokol pengiriman data"
        ],
        "answer": "A. Struktur fisik dan logis bagaimana perangkat saling terhubung"
    },
    {
        "q": "2️⃣ Topologi jaringan yang setiap komputer terhubung ke satu komputer pusat disebut?",
        "options": [
            "A. Topologi ring",
            "B. Topologi bus",
            "C. Topologi star",
            "D. Topologi mesh"
        ],
        "answer": "C. Topologi star"
    },
    {
        "q": "3️⃣ Topologi yang menggunakan satu jalur utama disebut?",
        "options": [
            "A. Star",
            "B. Bus",
            "C. Ring",
            "D. Mesh"
        ],
        "answer": "B. Bus"
    },
    {
        "q": "4️⃣ Kelebihan topologi star adalah?",
        "options": [
            "A. Murah dan mudah diatur",
            "B. Jika kabel utama rusak, semua koneksi putus",
            "C. Mudah menambah komputer baru tanpa mengganggu jaringan",
            "D. Semua komputer terhubung langsung satu sama lain"
        ],
        "answer": "C. Mudah menambah komputer baru tanpa mengganggu jaringan"
    },
    {
        "q": "5️⃣ Kekurangan utama topologi ring adalah?",
        "options": [
            "A. Jika satu komputer rusak, seluruh jaringan bisa terganggu",
            "B. Biaya tinggi",
            "C. Sulit dalam pengiriman data",
            "D. Tidak efisien untuk jaringan kecil"
        ],
        "answer": "A. Jika satu komputer rusak, seluruh jaringan bisa terganggu"
    }
]

# Menyimpan skor
score = 0
user_answers = []

# Menampilkan pertanyaan kuis
st.subheader("📘 Kuis Pemahaman")
for i, q in enumerate(questions):
    user_answer = st.radio(q["q"], q["options"], key=f"q{i}")
    user_answers.append(user_answer)
    if user_answer == q["answer"]:
        score += 20  # Nilai 20 poin per soal

# Tambahkan bagian refleksi/saran
st.markdown("---")
st.subheader("💬 Refleksi & Saran Pembelajaran Hari Ini")
feedback = st.text_area(
    "Tulis saran, kesan, atau masukan Anda terhadap pembelajaran hari ini:",
    placeholder="Contoh: Saya senang belajar topologi jaringan, tapi ingin lebih banyak praktik langsung...",
    height=150
)

# Tombol Simpan
if st.button("💾 Simpan & Lihat Hasil"):
    # Validasi identitas
    if not nama or not kelas or not absen:
        st.warning("⚠️ Harap isi nama, kelas, dan nomor absen terlebih dahulu.")
    else:
        # Menampilkan hasil kuis
        st.success(f"🎯 Nilai Anda: {score} / 100")
        if score == 100:
            st.balloons()
            st.info("Keren! Kamu menguasai topologi jaringan 🎉")
        elif score >= 60:
            st.warning("Cukup baik, tapi masih bisa lebih memahami konsep topologi!")
        else:
            st.error("Perlu belajar lagi ya. Coba pelajari kembali konsep dasarnya.")

        # Menampilkan saran audiens
        if feedback.strip() != "":
            st.markdown("---")
            st.subheader("📢 Terima kasih atas sarannya!")
            st.write(f"📝 \"{feedback}\"")
        else:
            st.warning("Kamu belum menuliskan saran atau masukan.")

        # Simpan ke file CSV
        data = {
            "Nama": [nama],
            "Kelas": [kelas],
            "Absen": [absen],
            "Jawaban": [user_answers],
            "Nilai": [score],
            "Saran": [feedback]
        }

        df = pd.DataFrame(data)

        if os.path.exists("hasil_refleksi.csv"):
            df.to_csv("hasil_refleksi.csv", mode='a', header=False, index=False)
        else:
            df.to_csv("hasil_refleksi.csv", index=False)

        st.info("💾 Jawaban dan saran Anda telah disimpan!")
import pandas as pd

# setelah data disimpan ke file CSV
df = pd.read_csv("data_refleksi.csv")

st.download_button(
    label="📥 Unduh Hasil Refleksi (CSV)",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name="data_refleksi.csv",
    mime="text/csv"
)



