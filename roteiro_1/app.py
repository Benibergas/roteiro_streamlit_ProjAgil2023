import streamlit as st

nome = st.text_input("Qual é seu nome?", '')

if st.button("Clique"):
    st.write(f'{nome}')
