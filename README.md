# AI Portrait Generator

live: https://ml-04-fi.streamlit.app/

Um dashboard Streamlit para geração de imagens de pessoas específicas usando IA generativa.

## Funcionalidades

- 🎨 Geração de imagens personalizadas com prompts detalhados
- 👤 Suporte para diferentes estilos de retrato
- 🎛️ Controles avançados de qualidade e estilo
- 📱 Interface responsiva e intuitiva
- 🔄 Histórico de gerações
- 💾 Download de imagens geradas
- 🎯 Templates de prompts pré-definidos

## Tecnologias

- **Streamlit**: Interface web interativa
- **OpenAI DALL-E**: Geração de imagens
- **Replicate**: APIs de modelos alternativos
- **Stability AI**: Stable Diffusion
- **UV**: Gerenciamento de dependências

## Instalação e Execução

### Usando UV (Recomendado)

```bash
# Criar ambiente virtual
uv venv

# Ativar ambiente virtual
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Instalar dependências
uv sync

# Executar aplicação
streamlit run src/main.py
```

### Usando Docker

```bash
# Build da imagem
docker build -t ai-portrait-generator .

# Executar container
docker run -p 8501:8501 -e OPENAI_API_KEY=your_key ai-portrait-generator
```

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=your_openai_api_key
REPLICATE_API_TOKEN=your_replicate_token
STABILITY_API_KEY=your_stability_key
```

## Uso

1. Acesse http://localhost:8501
2. Configure suas chaves de API
3. Digite sua descrição da pessoa/cena
4. Ajuste os parâmetros de geração
5. Clique em "Gerar Imagem"
6. Faça download do resultado

## Estrutura do Projeto

```
ai-portrait-generator/
├── src/
│   ├── main.py              # Aplicação principal
│   ├── generators/          # Módulos de geração
│   ├── utils/              # Utilitários
│   └── components/         # Componentes UI
├── templates/              # Templates de prompts
├── assets/                # Recursos estáticos
├── Dockerfile             # Container configuration
├── pyproject.toml         # Configuração do projeto
└── README.md             # Este arquivo
```