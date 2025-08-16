"""
AI Portrait Generator - Streamlit Dashboard
Aplicação principal para geração de imagens de pessoas usando IA
"""

import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da página
st.set_page_config(
    page_title="AI Portrait Generator",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Importar componentes
from components.sidebar import render_sidebar
from components.main_interface import render_main_interface
from components.gallery import render_gallery
from utils.session_state import initialize_session_state

def main():
    """Função principal da aplicação"""
    
    # Inicializar estado da sessão
    initialize_session_state()
    
    # Título principal
    st.title("🎨 AI Portrait Generator")
    st.markdown("---")
    
    # Layout em colunas
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Sidebar com configurações
        render_sidebar()
    
    with col2:
        # Interface principal
        render_main_interface()
    
    # Galeria de imagens geradas
    st.markdown("---")
    render_gallery()

if __name__ == "__main__":
    main()