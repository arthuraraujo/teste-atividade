"""
Templates de prompts pré-definidos para diferentes estilos
"""

PROMPT_TEMPLATES = {
    "Retrato Profissional": {
        "template": "Professional headshot portrait, high-quality studio lighting, clean background, business attire, confident expression, sharp focus, professional photography style",
        "description": "Ideal para fotos corporativas e LinkedIn"
    },
    
    "Estilo Artístico": {
        "template": "Artistic portrait, painterly style, dramatic lighting, creative composition, artistic interpretation, fine art photography, expressive mood",
        "description": "Estilo mais criativo e artístico"
    },
    
    "Fantasia/Ficção": {
        "template": "Fantasy character portrait, magical atmosphere, ethereal lighting, mystical elements, detailed costume design, fantasy art style, cinematic quality",
        "description": "Para personagens fantásticos e ficcionais"
    },
    
    "Vintage/Clássico": {
        "template": "Vintage portrait, classic photography style, timeless elegance, soft lighting, retro aesthetic, film photography look, nostalgic mood",
        "description": "Estilo clássico e atemporal"
    },
    
    "Moderno/Futurista": {
        "template": "Modern futuristic portrait, sleek design, contemporary style, high-tech elements, clean lines, minimalist aesthetic, cutting-edge fashion",
        "description": "Visual moderno e futurista"
    }
}

def get_template_prompt(template_name: str) -> str:
    """
    Retorna o prompt do template especificado
    
    Args:
        template_name: Nome do template
        
    Returns:
        String com o prompt do template ou string vazia
    """
    
    if template_name in PROMPT_TEMPLATES:
        return PROMPT_TEMPLATES[template_name]["template"]
    
    return ""

def get_template_description(template_name: str) -> str:
    """
    Retorna a descrição do template especificado
    
    Args:
        template_name: Nome do template
        
    Returns:
        String com a descrição do template
    """
    
    if template_name in PROMPT_TEMPLATES:
        return PROMPT_TEMPLATES[template_name]["description"]
    
    return ""

def get_all_templates() -> dict:
    """Retorna todos os templates disponíveis"""
    return PROMPT_TEMPLATES

def create_enhanced_prompt(base_prompt: str, template_name: str, enhancements: dict = None) -> str:
    """
    Cria um prompt aprimorado combinando template e melhorias
    
    Args:
        base_prompt: Prompt base do usuário
        template_name: Nome do template a aplicar
        enhancements: Dicionário com melhorias adicionais
        
    Returns:
        Prompt final combinado
    """
    
    template_prompt = get_template_prompt(template_name)
    
    if not template_prompt:
        return base_prompt
    
    # Combinar template com prompt base
    combined_prompt = f"{template_prompt}, {base_prompt}"
    
    # Aplicar melhorias se fornecidas
    if enhancements:
        quality_terms = enhancements.get('quality', [])
        style_terms = enhancements.get('style', [])
        technical_terms = enhancements.get('technical', [])
        
        if quality_terms:
            combined_prompt += f", {', '.join(quality_terms)}"
        
        if style_terms:
            combined_prompt += f", {', '.join(style_terms)}"
        
        if technical_terms:
            combined_prompt += f", {', '.join(technical_terms)}"
    
    return combined_prompt

# Melhorias padrão para diferentes contextos
DEFAULT_ENHANCEMENTS = {
    "quality": [
        "high resolution",
        "detailed",
        "sharp focus",
        "professional quality"
    ],
    
    "lighting": [
        "perfect lighting",
        "natural lighting",
        "studio lighting",
        "golden hour lighting",
        "dramatic lighting"
    ],
    
    "technical": [
        "8K resolution",
        "RAW photo",
        "professional photography",
        "DSLR quality",
        "award winning photography"
    ],
    
    "artistic": [
        "masterpiece",
        "artistic composition",
        "creative angle",
        "aesthetic",
        "visually striking"
    ]
}