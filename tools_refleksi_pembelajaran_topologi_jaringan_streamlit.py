import streamlit as st
import pandas as pd
import csv
import os

# --- Pengaturan halaman ---
st.set_page_config(page_title="Refleksi Pembelajaran Topologi Jaringan", layout="wide")

st.title("🧠 Refleksi Pembelajaran Topologi Jaringan")
st.markdown("Silakan isi identitas, jawab pertanyaan, dan berikan saran pembelajaran di bawah ini 👇")

# ==========================
# Bagian Identitas
# ==========================
st.subheader("🪪 Identitas Siswa")
col1, col2, col3 = st.columns(3)
with col1:
    nama = st.text_input("Nama Lengkap")
with col2:
    kelas = st.text_input("Kelas (contoh: XI TKJ 1)")
with col3:
    absen = st.text_input("Nomor Absen")

# ==========================
# Bagian Pertanyaan Refleksi
# ==========================
st.subheader("📘 Pertanyaan Refleksi dan Kuis")

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
        "options": ["A. Topologi ring", "B. Topologi bus", "C. Topologi star", "D. Topologi mesh"],
        "answer": "C. Topologi star"
    },
    {
        "q": "3️⃣ Topologi yang menggunakan satu jalur utama disebut?",
        "options": ["A. Star", "B. Bus", "C. Ring", "D. Mesh"],
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

user_answers = []
score = 0

for i, q in enumerate(questions):
    answer = st.radio(q["q"], q["options"], key=f"q{i}")
    user_answers.append(answer)
    if answer == q["answer"]:
        score += 20  # total 5 pertanyaan × 20 = 100

# ==========================
# Bagian Refleksi / Saran
# ==========================
st.markdown("---")
st.subheader("💬 Saran Pembelajaran Hari Ini")
feedback = st.text_area(
    "Tuliskan saran atau masukan kamu terhadap pembelajaran hari ini:",
    placeholder="Contoh: Pembelajarannya menarik, tapi saya ingin lebih banyak praktik...",
    height=150
)

# ==========================
# Simpan ke file CSV
# ==========================
csv_path = "data_refleksi.csv"

if st.button("💾 Simpan Jawaban"):
    if not nama or not kelas or not absen:
        st.warning("⚠️ Harap isi nama, kelas, dan nomor absen sebelum menyimpan.")
    else:
        header = ["Nama", "Kelas", "Absen", "Jawaban", "Nilai", "Saran"]
        data = [nama, kelas, absen, str(user_answers), score, feedback]

        file_exists = os.path.exists(csv_path)
        with open(csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists or os.stat(csv_path).st_size == 0:  # jika file kosong/tidak ada
                writer.writerow(header)
            writer.writerow(data)

        st.success(f"✅ Jawaban kamu sudah disimpan! Nilai kamu: **{score} / 100**")

# ==========================
# Menampilkan data hasil refleksi & peringkat
# ==========================
st.markdown("---")
st.subheader("📊 Hasil Refleksi Keseluruhan")

if os.path.exists(csv_path) and os.stat(csv_path).st_size > 0:
    try:
        df = pd.read_csv(csv_path)
        if not df.empty:
            st.dataframe(df, use_container_width=True)

            st.download_button(
                label="📥 Unduh Semua Jawaban (CSV)",
                data=df.to_csv(index=False).encode('utf-8-sig'),
                file_name="data_refleksi.csv",
                mime="text/csv"
            )

            # ==========================
            # 🎯 Peringkat Responden
            # ==========================
            st.markdown("---")
            st.subheader("🏆 Peringkat Responden Berdasarkan Nilai")

            if "Nilai" in df.columns:
                df["Nilai"] = pd.to_numeric(df["Nilai"], errors="coerce").fillna(0)
                ranking = df.sort_values(by="Nilai", ascending=False)
                ranking["Peringkat"] = range(1, len(ranking) + 1)
                tampil = ranking[["Peringkat", "Nama", "Kelas", "Absen", "Nilai"]]
                st.dataframe(tampil, use_container_width=True)

                top3 = tampil.head(3)
                st.markdown("### 🥇 Peringkat 3 Teratas:")
                for i, row in top3.iterrows():
                    if row["Peringkat"] == 1:
                        st.success(f"🥇 {row['Nama']} — {row['Kelas']} (Nilai: {row['Nilai']})")
                    elif row["Peringkat"] == 2:
                        st.info(f"🥈 {row['Nama']} — {row['Kelas']} (Nilai: {row['Nilai']})")
                    elif row["Peringkat"] == 3:
                        st.warning(f"🥉 {row['Nama']} — {row['Kelas']} (Nilai: {row['Nilai']})")
            else:
                st.info("⚠️ Kolom 'Nilai' belum ditemukan di file data. Jawaban baru akan otomatis menambahkan kolom ini.")
        else:
            st.info("ℹ️ Belum ada data refleksi yang tersimpan.")
    except pd.errors.EmptyDataError:
        st.info("ℹ️ Belum ada data refleksi yang tersimpan.")
else:
    st.info("ℹ️ Belum ada data refleksi yang tersimpan.")
