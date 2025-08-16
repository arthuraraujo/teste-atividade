"""
Componente de galeria para mostrar histórico de gerações
"""

import streamlit as st
import time
from datetime import datetime

def render_gallery():
    """Renderiza a galeria de imagens geradas"""
    
    if 'generation_history' not in st.session_state or not st.session_state.generation_history:
        st.info("📸 Nenhuma imagem gerada ainda. Use o gerador acima para começar!")
        return
    
    st.header("🖼️ Galeria de Gerações")
    
    # Controles da galeria
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f"**{len(st.session_state.generation_history)} gerações no histórico**")
    
    with col2:
        if st.button("🗑️ Limpar Histórico"):
            st.session_state.generation_history = []
            st.rerun()
    
    with col3:
        show_details = st.checkbox("📋 Mostrar Detalhes", value=False)
    
    # Mostrar histórico (mais recente primeiro)
    history = reversed(st.session_state.generation_history)
    
    for i, generation in enumerate(history):
        with st.container():
            st.markdown("---")
            
            # Cabeçalho da geração
            timestamp = datetime.fromtimestamp(generation['timestamp'])
            st.markdown(f"**Geração #{len(st.session_state.generation_history) - i}** - {timestamp.strftime('%d/%m/%Y %H:%M')}")
            
            # Layout das imagens
            images = generation['images']
            
            if len(images) == 1:
                # Uma imagem
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.image(images[0], use_column_width=True)
                
                with col2:
                    if show_details:
                        st.markdown("**Detalhes:**")
                        st.markdown(f"- Modelo: {generation['model']}")
                        st.markdown(f"- Qualidade: {generation['parameters']['quality']}")
                        st.markdown(f"- Tamanho: {generation['parameters']['size']}")
                        st.markdown(f"- Estilo: {generation['parameters']['style']}")
                    
                    # Botões de ação
                    st.download_button(
                        "💾 Download",
                        data=images[0],
                        file_name=f"portrait_gallery_{int(generation['timestamp'])}.png",
                        mime="image/png",
                        key=f"gallery_download_{i}",
                        use_container_width=True
                    )
                    
                    if st.button("🔄 Reutilizar Prompt", key=f"reuse_{i}", use_container_width=True):
                        # Copiar prompt para área de texto (simulado)
                        st.info("💡 Copie o prompt abaixo e cole no gerador")
            
            else:
                # Múltiplas imagens
                cols = st.columns(min(len(images), 3))
                
                for j, image in enumerate(images):
                    with cols[j % 3]:
                        st.image(image, use_column_width=True)
                        st.download_button(
                            f"💾 {j+1}",
                            data=image,
                            file_name=f"portrait_gallery_{int(generation['timestamp'])}_{j+1}.png",
                            mime="image/png",
                            key=f"gallery_download_{i}_{j}",
                            use_container_width=True
                        )
            
            # Mostrar prompt
            with st.expander(f"📝 Ver prompt da geração #{len(st.session_state.generation_history) - i}"):
                st.code(generation['prompt'])
                
                # Botão para copiar prompt
                if st.button("📋 Copiar Prompt", key=f"copy_prompt_{i}"):
                    # Em uma aplicação real, isso copiaria para o clipboard
                    st.success("Prompt copiado! (funcionalidade simulada)")

def render_saved_prompts():
    """Renderiza seção de prompts salvos"""
    
    if 'saved_prompts' not in st.session_state or not st.session_state.saved_prompts:
        return
    
    st.subheader("💾 Prompts Salvos")
    
    for i, prompt in enumerate(st.session_state.saved_prompts):
        with st.expander(f"Prompt {i+1}: {prompt[:50]}..."):
            st.code(prompt)
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                if st.button("🎨 Usar Este Prompt", key=f"use_saved_{i}"):
                    st.info("💡 Copie o prompt acima e cole no gerador")
            
            with col2:
                if st.button("🗑️ Remover", key=f"remove_saved_{i}"):
                    st.session_state.saved_prompts.pop(i)
                    st.rerun()