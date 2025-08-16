"""
Gerenciamento do estado da sessão Streamlit
"""

import streamlit as st

def initialize_session_state():
    """Inicializa variáveis do estado da sessão"""
    
    # Chaves de API
    if 'openai_key' not in st.session_state:
        st.session_state.openai_key = ""
    
    if 'replicate_key' not in st.session_state:
        st.session_state.replicate_key = ""
    
    if 'stability_key' not in st.session_state:
        st.session_state.stability_key = ""
    
    # Configurações do modelo
    if 'selected_model' not in st.session_state:
        st.session_state.selected_model = "DALL-E 3"
    
    if 'quality' not in st.session_state:
        st.session_state.quality = "hd"
    
    if 'image_size' not in st.session_state:
        st.session_state.image_size = "1024x1024"
    
    if 'style' not in st.session_state:
        st.session_state.style = "vivid"
    
    if 'num_images' not in st.session_state:
        st.session_state.num_images = 1
    
    # Template
    if 'template_choice' not in st.session_state:
        st.session_state.template_choice = "Personalizado"
    
    # Configurações avançadas
    if 'seed' not in st.session_state:
        st.session_state.seed = None
    
    if 'negative_prompt' not in st.session_state:
        st.session_state.negative_prompt = ""
    
    # Histórico
    if 'generation_history' not in st.session_state:
        st.session_state.generation_history = []
    
    if 'saved_prompts' not in st.session_state:
        st.session_state.saved_prompts = []

def reset_session_state():
    """Reseta o estado da sessão"""
    
    keys_to_keep = ['openai_key', 'replicate_key', 'stability_key']
    
    for key in list(st.session_state.keys()):
        if key not in keys_to_keep:
            del st.session_state[key]
    
    initialize_session_state()

def export_session_data():
    """Exporta dados da sessão para backup"""
    
    export_data = {
        'generation_history': st.session_state.get('generation_history', []),
        'saved_prompts': st.session_state.get('saved_prompts', []),
        'settings': {
            'selected_model': st.session_state.get('selected_model'),
            'quality': st.session_state.get('quality'),
            'image_size': st.session_state.get('image_size'),
            'style': st.session_state.get('style'),
            'num_images': st.session_state.get('num_images'),
            'template_choice': st.session_state.get('template_choice')
        }
    }
    
    return export_data