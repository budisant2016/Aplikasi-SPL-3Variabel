import streamlit as st

st.title("Aplikasi Web Solusi SPL 3 Variabel dg Eliminasi Gauss")
st.write(
    "Isikan masing-masing indeks variabel x1-x3."
)
a1 = st.number_input("Masukkan indeks variabel A1:", min_value=0, max_value=100)
