import streamlit as st

st.title("Roteiro 2: Widgets Interativos")

value_slider = st.slider("Escolha um valor", 0, 100)
value_checkbox = st.checkbox('Eu aceito')
value_radio = st.radio('O que vc prefere', ['Gato', 'Cachorro', 'Papagaio'])
value_selectbox = st.selectbox('Qual conta vc quer acessar?', ('Beni Sliozbergas', 'BeniS', 'Benisli'))
value_toggle = st.toggle('Vc está mentindo')
if st.button("Mostrar valor do slider"):
    st.write(f"{value_slider, value_checkbox, value_radio, value_selectbox, value_toggle}")
