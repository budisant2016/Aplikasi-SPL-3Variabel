import streamlit as st

st.title("Aplikasi Web Solusi SPL 3 Variabel dg Eliminasi Gauss")
st.write("A1 X1 + A2 X2 + A3 X3 = B1")
st.write("A4 X1 + A5 X2 + A6 X3 = B2")
st.write("A7 X1 + A8 X2 + A9 X3 = B3")
st.write(
    "Isikan masing-masing indeks variabel x1-x3."
)

a1 = st.number_input("Masukkan indeks variabel A1:", min_value=0, max_value=100)
a2 = st.number_input("Masukkan indeks variabel A2:", min_value=0, max_value=100)
a3 = st.number_input("Masukkan indeks variabel A3:", min_value=0, max_value=100)
a4 = st.number_input("Masukkan indeks variabel A4:", min_value=0, max_value=100)
a5 = st.number_input("Masukkan indeks variabel A5:", min_value=0, max_value=100)
a6 = st.number_input("Masukkan indeks variabel A6:", min_value=0, max_value=100)
a7 = st.number_input("Masukkan indeks variabel A7:", min_value=0, max_value=100)
a8 = st.number_input("Masukkan indeks variabel A8:", min_value=0, max_value=100)
a9 = st.number_input("Masukkan indeks variabel A9:", min_value=0, max_value=100)
b1 = st.number_input("Masukkan indeks variabel B1:", min_value=0, max_value=100)
b2 = st.number_input("Masukkan indeks variabel B2:", min_value=0, max_value=100)
b3 = st.number_input("Masukkan indeks variabel B3:", min_value=0, max_value=100)
