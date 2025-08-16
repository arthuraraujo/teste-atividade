"""
Módulo principal para geração de imagens usando diferentes APIs de IA
"""

import openai
import requests
from PIL import Image
import io
import base64
from typing import Dict, List, Any

def generate_image(
    prompt: str,
    model: str,
    api_key: str,
    quality: str = "hd",
    size: str = "1024x1024",
    style: str = "vivid",
    num_images: int = 1,
    **kwargs
) -> Dict[str, Any]:
    """
    Gera imagem usando o modelo especificado
    
    Args:
        prompt: Descrição da imagem a ser gerada
        model: Modelo de IA a usar
        api_key: Chave da API
        quality: Qualidade da imagem
        size: Tamanho da imagem
        style: Estilo da imagem
        num_images: Número de imagens a gerar
        
    Returns:
        Dict com success, images (lista de bytes) e error
    """
    
    try:
        if model.startswith("DALL-E"):
            return generate_with_dalle(
                prompt=prompt,
                api_key=api_key,
                model=model,
                quality=quality,
                size=size,
                style=style,
                num_images=num_images
            )
        
        elif model == "Stable Diffusion XL":
            return generate_with_stability(
                prompt=prompt,
                api_key=api_key,
                size=size,
                num_images=num_images
            )
        
        elif model == "Midjourney (Replicate)":
            return generate_with_replicate(
                prompt=prompt,
                api_key=api_key,
                size=size,
                num_images=num_images
            )
        
        else:
            return {
                "success": False,
                "error": f"Modelo não suportado: {model}",
                "images": []
            }
            
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "images": []
        }

def generate_with_dalle(
    prompt: str,
    api_key: str,
    model: str,
    quality: str,
    size: str,
    style: str,
    num_images: int
) -> Dict[str, Any]:
    """Gera imagem usando DALL-E"""
    
    try:
        client = openai.OpenAI(api_key=api_key)
        
        # Determinar versão do modelo
        dalle_model = "dall-e-3" if model == "DALL-E 3" else "dall-e-2"
        
        # DALL-E 3 só suporta 1 imagem por vez
        if dalle_model == "dall-e-3":
            num_images = 1
        
        response = client.images.generate(
            model=dalle_model,
            prompt=prompt,
            size=size,
            quality=quality if dalle_model == "dall-e-3" else "standard",
            style=style if dalle_model == "dall-e-3" else None,
            n=num_images,
            response_format="url"
        )
        
        # Baixar imagens
        images = []
        for image_data in response.data:
            img_response = requests.get(image_data.url)
            if img_response.status_code == 200:
                images.append(img_response.content)
        
        return {
            "success": True,
            "images": images,
            "error": None
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Erro DALL-E: {str(e)}",
            "images": []
        }

def generate_with_stability(
    prompt: str,
    api_key: str,
    size: str,
    num_images: int
) -> Dict[str, Any]:
    """Gera imagem usando Stability AI"""
    
    try:
        # Converter tamanho para formato Stability
        width, height = map(int, size.split('x'))
        
        url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
        
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        
        body = {
            "text_prompts": [
                {
                    "text": prompt,
                    "weight": 1
                }
            ],
            "cfg_scale": 7,
            "height": height,
            "width": width,
            "samples": num_images,
            "steps": 30,
        }
        
        response = requests.post(url, headers=headers, json=body)
        
        if response.status_code != 200:
            return {
                "success": False,
                "error": f"Stability API error: {response.status_code}",
                "images": []
            }
        
        data = response.json()
        images = []
        
        for artifact in data["artifacts"]:
            image_data = base64.b64decode(artifact["base64"])
            images.append(image_data)
        
        return {
            "success": True,
            "images": images,
            "error": None
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Erro Stability: {str(e)}",
            "images": []
        }

def generate_with_replicate(
    prompt: str,
    api_key: str,
    size: str,
    num_images: int
) -> Dict[str, Any]:
    """Gera imagem usando Replicate (Midjourney style)"""
    
    try:
        import replicate
        
        # Configurar cliente
        replicate.Client(api_token=api_key)
        
        # Usar modelo Midjourney-style no Replicate
        output = replicate.run(
            "prompthero/openjourney:9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb",
            input={
                "prompt": prompt,
                "width": int(size.split('x')[0]),
                "height": int(size.split('x')[1]),
                "num_outputs": num_images,
                "num_inference_steps": 50,
                "guidance_scale": 7.5
            }
        )
        
        # Baixar imagens
        images = []
        for url in output:
            img_response = requests.get(url)
            if img_response.status_code == 200:
                images.append(img_response.content)
        
        return {
            "success": True,
            "images": images,
            "error": None
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Erro Replicate: {str(e)}",
            "images": []
        }