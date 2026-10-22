 Sistema de Recuperacion Semantica Local (RAG) - TP 3

Este proyecto implementa un sistema RAG (Retrieval-Augmented Generation) asincrono y persistente utilizando LangChain, ChromaDB, Sentence-Transformers y Pydantic.

## Caracteristicas
* Ingesta y Chunking: Procesa archivos de data/ usando RecursiveCharacterTextSplitter (500 tokens, 50 overlap) y genera embeddings con all-MiniLM-L6-v2.
* Persistencia Vectorial: Almacena los vectores en ./vectorstore evitando la reindexacion si la base ya existe.
* Filtro Anti-Alucinacion: Prompt calibrado para responder estrictamente con el contexto y declarar falta de informacion ante consultas fuera de dominio.
* Salida Estructurada: Formato validado con Pydantic (RespuestaRAG).

## Instalacion y Uso

1. Instalar dependencias:
   pip install -r requirements.txt

2. Configurar variables de entorno (.env):
   DEFAULT_PROVIDER=openai
   DEFAULT_MODEL=openai/gpt-oss-120b
   OPENAI_API_KEY=tu_api_key_aqui
   OPENAI_BASE_URL=https://api.groq.com/openai/v1

3. Ejecutar pruebas:
   python main.py