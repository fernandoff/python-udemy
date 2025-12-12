import streamlit as st
import dados

st.title("Filmes")

nome = st.text_input("Nome do filme:")
ano = st.number_input("Ano do Filme:", min_value=2010, max_value=2024)
nota = st.slider("Nota do filme:", min_value=0.0, max_value=10.0)

if st.button('Adicionar'):
    if nome.strip() == "":
        st.error("Por favor, digite o nome do filme.")
    elif dados.insere_dados(nome, ano, nota):        
        st.success("Filme cadastrado com sucesso!")
        st.rerun()
    else:
        st.error(f"O filme '{nome}' já está cadastrado!")
    
filmes = dados.obter_dados()
st.header("Lista de Filmes")
st.table(filmes)

st.header("Excluir Filme")
if filmes:
    filme_ids = [f[0] for f in filmes]
    filme_nomes = [f"{f[0]} - {f[1]}" for f in filmes]
    filme_selecionado = st.selectbox("Selecione o filme para excluir:", range(len(filme_ids)), format_func=lambda x: filme_nomes[x])
    
    if st.button('Excluir Filme'):
        dados.exclui_dados(filme_ids[filme_selecionado])
        st.success("Filme excluído com sucesso!")
        st.rerun()
else:
    st.info("Nenhum filme cadastrado.")