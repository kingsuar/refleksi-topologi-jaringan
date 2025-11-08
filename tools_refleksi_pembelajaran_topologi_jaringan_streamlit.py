import streamlit as st

st.set_page_config(page_title="Refleksi Pembelajaran Topologi Jaringan", layout="wide")

st.title("🧠 Refleksi Pembelajaran Topologi Jaringan")

st.markdown("""
Selamat datang di **alat refleksi pembelajaran topologi jaringan**.  
Silakan jawab pertanyaan di bawah ini dengan jujur untuk membantu evaluasi pemahaman Anda hari ini.
""")

# Pertanyaan
questions = [
    "1️⃣ Apa yang Anda pahami tentang topologi jaringan?",
    "2️⃣ Sebutkan jenis-jenis topologi jaringan yang Anda ketahui.",
    "3️⃣ Topologi jaringan manakah yang paling efisien menurut Anda? Mengapa?",
    "4️⃣ Apa manfaat memahami topologi jaringan dalam dunia nyata?",
    "5️⃣ Apa hal yang paling menarik dari pembelajaran hari ini?"
]

answers = []

for q in questions:
    ans = st.text_area(q, placeholder="Tulis jawaban Anda di sini...", height=100)
    answers.append(ans)

if st.button("💾 Simpan Jawaban"):
    if all(answers):
        st.success("✅ Terima kasih! Semua jawaban telah disimpan (simulasi).")
        st.session_state["finished"] = True
    else:
        st.warning("⚠️ Harap isi semua pertanyaan sebelum menyimpan.")

# Halaman saran setelah menjawab
if st.session_state.get("finished", False):
    st.markdown("---")
    st.subheader("💡 Saran Pembelajaran Hari Ini")
    st.markdown("""
- Pelajari kembali konsep dasar **topologi jaringan (fisik dan logis)**.  
- Cobalah menggambar diagram sederhana dari **topologi bus, ring, dan star**.  
- Diskusikan dengan teman untuk membandingkan kelebihan masing-masing.  
- Lanjutkan dengan mempelajari **implementasi topologi dalam jaringan nyata (LAN, MAN, WAN)**.
    """)

    st.success("🌟 Terus semangat belajar dan berefleksi setiap hari!")
