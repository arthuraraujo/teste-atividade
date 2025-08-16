#!/bin/bash

# Script para executar o AI Portrait Generator

echo "🎨 AI Portrait Generator - Setup"
echo "================================"

# Verificar se uv está instalado
if ! command -v uv &> /dev/null; then
    echo "❌ UV não encontrado. Instalando..."
    pip install uv
fi

# Criar ambiente virtual se não existir
if [ ! -d ".venv" ]; then
    echo "📦 Criando ambiente virtual..."
    uv venv
fi

# Instalar dependências usando uv pip
echo "📥 Instalando dependências..."
uv pip install streamlit openai pillow requests python-dotenv

# Verificar se arquivo .env existe
if [ ! -f ".env" ]; then
    echo "⚠️  Arquivo .env não encontrado!"
    echo "📋 Copiando .env.example para .env..."
    cp .env.example .env
    echo "✏️  Por favor, edite o arquivo .env com suas chaves de API"
    echo ""
fi

# Executar aplicação
echo "🚀 Iniciando aplicação..."
echo "📱 Acesse: http://localhost:8501"
echo ""

# Usar uv para executar streamlit
uv run streamlit run src/main.py