import streamlit as st

st.title("🎈nasayy")
st.image("IMG_20250514_115129.jpg", width=200)
st.subheader("Hendri Setiadi, S.Tr.Kom")

#with col1:
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
