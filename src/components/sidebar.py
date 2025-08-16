"""
Componente da sidebar com configurações e controles
"""

import streamlit as st
import os

def render_sidebar():
    """Renderiza a sidebar com configurações"""
    
    st.header("⚙️ Configurações")
    
    # Configurações de API
    with st.expander("🔑 Chaves de API", expanded=True):
        openai_key = st.text_input(
            "OpenAI API Key",
            value=os.getenv("OPENAI_API_KEY", ""),
            type="password",
            help="Chave para usar DALL-E"
        )
        
        replicate_key = st.text_input(
            "Replicate API Token",
            value=os.getenv("REPLICATE_API_TOKEN", ""),
            type="password",
            help="Token para modelos do Replicate"
        )
        
        stability_key = st.text_input(
            "Stability API Key",
            value=os.getenv("STABILITY_API_KEY", ""),
            type="password",
            help="Chave para Stable Diffusion"
        )
        
        # Salvar chaves na sessão
        st.session_state.openai_key = openai_key
        st.session_state.replicate_key = replicate_key
        st.session_state.stability_key = stability_key
    
    # Seleção do modelo
    st.subheader("🤖 Modelo de IA")
    model_choice = st.selectbox(
        "Escolha o modelo:",
        ["DALL-E 3", "DALL-E 2", "Stable Diffusion XL", "Midjourney (Replicate)"],
        help="Diferentes modelos têm estilos únicos"
    )
    st.session_state.selected_model = model_choice
    
    # Parâmetros de geração
    st.subheader("🎛️ Parâmetros")
    
    # Qualidade
    quality = st.select_slider(
        "Qualidade",
        options=["standard", "hd"],
        value="hd",
        help="HD produz imagens de maior qualidade"
    )
    st.session_state.quality = quality
    
    # Tamanho da imagem
    size = st.selectbox(
        "Tamanho",
        ["1024x1024", "1792x1024", "1024x1792"],
        help="Formato quadrado ou retangular"
    )
    st.session_state.image_size = size
    
    # Estilo
    style = st.selectbox(
        "Estilo",
        ["vivid", "natural"],
        help="Vivid: mais dramático, Natural: mais realista"
    )
    st.session_state.style = style
    
    # Número de imagens
    num_images = st.slider(
        "Número de imagens",
        min_value=1,
        max_value=4,
        value=1,
        help="Quantas variações gerar"
    )
    st.session_state.num_images = num_images
    
    # Templates de prompt
    st.subheader("📝 Templates")
    template_choice = st.selectbox(
        "Template de prompt:",
        [
            "Personalizado",
            "Retrato Profissional",
            "Estilo Artístico",
            "Fantasia/Ficção",
            "Vintage/Clássico",
            "Moderno/Futurista"
        ]
    )
    st.session_state.template_choice = template_choice
    
    # Configurações avançadas
    with st.expander("🔧 Avançado"):
        seed = st.number_input(
            "Seed (opcional)",
            min_value=0,
            max_value=999999,
            value=0,
            help="Para reproduzir resultados específicos"
        )
        st.session_state.seed = seed if seed > 0 else None
        
        negative_prompt = st.text_area(
            "Prompt negativo",
            placeholder="O que NÃO incluir na imagem...",
            help="Elementos a evitar na geração"
        )
        st.session_state.negative_prompt = negative_prompt