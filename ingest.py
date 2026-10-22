import os
import logging
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("ingest")

PERSIST_DIRECTORY = "./vectorstore"


def get_embeddings():
    """Usa un modelo de embeddings local (MiniLM) para no depender de llamadas a API externa."""
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def run_ingestion(data_dir: str = "./data"):
    if os.path.exists(PERSIST_DIRECTORY) and os.listdir(PERSIST_DIRECTORY):
        logger.info(f"⚡ Base vectorial encontrada en '{PERSIST_DIRECTORY}'. Omitiendo re-indexación.")
        embeddings = get_embeddings()
        return Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings)

    logger.info(f"📂 Cargar documentos desde '{data_dir}'...")
    loader = DirectoryLoader(data_dir, glob="*.txt", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
    docs = loader.load()

    if not docs:
        raise FileNotFoundError(f"No se encontraron archivos .txt en '{data_dir}'.")

    logger.info(f"✂️ Aplicando chunking a {len(docs)} documentos...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    chunks = text_splitter.split_documents(docs)

    logger.info("💾 Guardando embeddings en ChromaDB local...")
    embeddings = get_embeddings()
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )
    logger.info("✅ Persistencia en ChromaDB completada.")
    return vectorstore