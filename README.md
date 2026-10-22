# Sistema de Recuperaci車n Sem芍ntica Local (RAG) - TP 3

Este proyecto implementa un sistema **RAG (Retrieval-Augmented Generation)** as赤ncrono y persistente utilizando **LangChain**, **ChromaDB**, **Sentence-Transformers** y **Pydantic**.

## ?? Caracter赤sticas
* **Ingesta y Chunking**: Procesa archivos de `data/` usando `RecursiveCharacterTextSplitter` (500 tokens, 50 overlap) y genera embeddings con `all-MiniLM-L6-v2`.
* **Persistencia Vectorial**: Almacena los vectores en `./vectorstore` evitando la reindexaci車n si la base ya existe.
* **Filtro Anti-Alucinaci車n**: Prompt calibrado para responder estrictamente con el contexto y declarar falta de informaci車n ante consultas fuera de dominio.
* **Salida Estructurada**: Formato validado con Pydantic (`RespuestaRAG`).

## ??? Instalaci車n y Uso

1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt