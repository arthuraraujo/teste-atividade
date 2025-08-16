"""
Interface principal para entrada de prompts e geração de imagens
"""

import streamlit as st
from generators.image_generator import generate_image
from utils.prompt_templates import get_template_prompt
import time

def render_main_interface():
    """Renderiza a interface principal"""
    
    st.header("✨ Gerador de Retratos")
    
    # Área de prompt
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Campo de texto principal
        user_prompt = st.text_area(
            "Descreva a pessoa e a cena:",
            height=150,
            placeholder="Ex: Uma mulher de 30 anos, cabelos castanhos ondulados, olhos verdes, sorrindo suavemente, usando um vestido azul elegante, em um jardim com flores coloridas ao fundo, luz dourada do pôr do sol...",
            help="Seja específico sobre características físicas, roupas, cenário e iluminação"
        )
        
        # Aplicar template se selecionado
        if st.session_state.get('template_choice', 'Personalizado') != 'Personalizado':
            template_prompt = get_template_prompt(st.session_state.template_choice)
            if template_prompt and user_prompt:
                combined_prompt = f"{template_prompt}, {user_prompt}"
                st.info(f"📝 Template aplicado: {st.session_state.template_choice}")
            else:
                combined_prompt = user_prompt
        else:
            combined_prompt = user_prompt
    
    with col2:
        st.markdown("### 💡 Dicas")
        st.markdown("""
        **Características físicas:**
        - Idade aproximada
        - Cor e estilo do cabelo
        - Cor dos olhos
        - Expressão facial
        
        **Roupas e acessórios:**
        - Estilo de roupa
        - Cores predominantes
        - Joias ou acessórios
        
        **Cenário:**
        - Local (interno/externo)
        - Iluminação
        - Elementos de fundo
        """)
    
    # Botões de ação
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        generate_btn = st.button(
            "🎨 Gerar Imagem",
            type="primary",
            disabled=not combined_prompt or not st.session_state.get('openai_key'),
            use_container_width=True
        )
    
    with col2:
        if st.button("🔄 Limpar", use_container_width=True):
            st.rerun()
    
    with col3:
        if st.button("💾 Salvar Prompt", use_container_width=True):
            if combined_prompt:
                if 'saved_prompts' not in st.session_state:
                    st.session_state.saved_prompts = []
                st.session_state.saved_prompts.append(combined_prompt)
                st.success("Prompt salvo!")
    
    # Área de geração
    if generate_btn and combined_prompt:
        if not st.session_state.get('openai_key'):
            st.error("❌ Por favor, configure sua chave da OpenAI na sidebar")
            return
        
        # Mostrar prompt final
        with st.expander("📝 Prompt final enviado para IA"):
            st.code(combined_prompt)
        
        # Área de progresso
        progress_container = st.container()
        
        with progress_container:
            st.info("🎨 Gerando imagem... Isso pode levar alguns segundos.")
            progress_bar = st.progress(0)
            
            # Simular progresso
            for i in range(100):
                time.sleep(0.02)
                progress_bar.progress(i + 1)
        
        # Gerar imagem
        try:
            result = generate_image(
                prompt=combined_prompt,
                model=st.session_state.selected_model,
                api_key=st.session_state.openai_key,
                quality=st.session_state.quality,
                size=st.session_state.image_size,
                style=st.session_state.style,
                num_images=st.session_state.num_images
            )
            
            progress_container.empty()
            
            if result['success']:
                st.success("✅ Imagem gerada com sucesso!")
                
                # Salvar no histórico
                if 'generation_history' not in st.session_state:
                    st.session_state.generation_history = []
                
                st.session_state.generation_history.append({
                    'prompt': combined_prompt,
                    'images': result['images'],
                    'timestamp': time.time(),
                    'model': st.session_state.selected_model,
                    'parameters': {
                        'quality': st.session_state.quality,
                        'size': st.session_state.image_size,
                        'style': st.session_state.style
                    }
                })
                
                # Mostrar imagens
                display_generated_images(result['images'], combined_prompt)
                
            else:
                st.error(f"❌ Erro na geração: {result['error']}")
                
        except Exception as e:
            progress_container.empty()
            st.error(f"❌ Erro inesperado: {str(e)}")

def display_generated_images(images, prompt):
    """Exibe as imagens geradas"""
    
    st.markdown("### 🖼️ Resultado")
    
    if len(images) == 1:
        # Uma imagem
        st.image(images[0], caption=prompt[:100] + "...", use_column_width=True)
        
        # Botão de download
        col1, col2 = st.columns([1, 1])
        with col1:
            st.download_button(
                "💾 Download",
                data=images[0],
                file_name=f"portrait_{int(time.time())}.png",
                mime="image/png",
                use_container_width=True
            )
        with col2:
            if st.button("🔄 Gerar Variação", use_container_width=True):
                st.info("Funcionalidade em desenvolvimento")
    
    else:
        # Múltiplas imagens
        cols = st.columns(min(len(images), 2))
        
        for i, image in enumerate(images):
            with cols[i % 2]:
                st.image(image, caption=f"Variação {i+1}", use_column_width=True)
                st.download_button(
                    f"💾 Download {i+1}",
                    data=image,
                    file_name=f"portrait_{int(time.time())}_{i+1}.png",
                    mime="image/png",
                    key=f"download_{i}",
                    use_container_width=True
                )