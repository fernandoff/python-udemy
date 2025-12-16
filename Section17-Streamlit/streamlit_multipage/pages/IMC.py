import streamlit as st

st.title("Projetos")

import streamlit as st

st.title("Calculadora IMC")

peso = st.number_input("Digite o seu peso (em kg)", min_value=0.0, format="%.2f")

status = st.radio("Selecione a opção de altura", ("cms", "metros"))

imc = None

if status == "cms":
    altura = st.number_input("Digite a altura em centímetros", min_value=0.0, format="%.2f")
    if altura > 0:
        imc = peso / ((altura / 100) ** 2)

elif status == "metros":
    altura = st.number_input("Digite a altura em metros", min_value=0.0, format="%.2f")
    if altura > 0:
        imc = peso / (altura ** 2)

if st.button("Calcular IMC") and imc is not None:
    st.text(f"Seu índice de IMC é {imc:.2f}")

    if imc < 16:
        st.error("Extremamente abaixo do peso")
    elif imc < 18.5:
        st.warning("Abaixo do peso")
    elif imc < 25:
        st.success("Saudável")
    elif imc < 30:
        st.warning("Excesso de peso")
    else:
        st.error("Extremamente acima do peso")


st.title("Calculadora IMC")