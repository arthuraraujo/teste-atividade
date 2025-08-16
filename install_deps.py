#!/usr/bin/env python3
"""
Script para instalar dependências básicas do projeto
"""

import subprocess
import sys
import os

def run_command(cmd):
    """Executa comando e mostra output"""
    print(f"🔧 Executando: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
    return result.returncode == 0

def main():
    """Instala dependências básicas"""
    
    # Verificar se estamos no venv
    if not os.path.exists('.venv'):
        print("❌ Ambiente virtual não encontrado. Execute: uv venv")
        return False
    
    # Ativar venv e instalar dependências básicas
    venv_python = ".venv/bin/python"
    venv_pip = ".venv/bin/pip"
    
    dependencies = [
        "streamlit>=1.29.0",
        "openai>=1.3.0",
        "pillow>=10.0.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0"
    ]
    
    print("📦 Instalando dependências básicas...")
    
    for dep in dependencies:
        success = run_command([venv_pip, "install", dep])
        if not success:
            print(f"❌ Falha ao instalar {dep}")
            return False
    
    print("✅ Dependências instaladas com sucesso!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)