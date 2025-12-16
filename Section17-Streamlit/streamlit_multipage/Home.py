import streamlit as st
import os
from pathlib import Path

st.set_page_config(
    page_title="Multipage App"
)

st.title("Home Page")
st.sidebar.success("Escolha a Página")

# Obtém o diretório do arquivo atual
current_dir = Path(__file__).parent
pages_dir = current_dir / "pages"

# Lista os arquivos .py no diretório pages
if pages_dir.exists():
    st.write("### Páginas Disponíveis:")
    page_files = [f for f in os.listdir(pages_dir) if f.endswith('.py')]
    
    for page_file in sorted(page_files):
        page_name = page_file.replace('.py', '').replace('_', ' ')
        page_path = f"pages/{page_file}"
        st.page_link(page_path, label=f"📄 {page_name}")
else:
    st.write("Diretório 'pages' não encontrado.")


