
import os
from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.rag_doc_ingestion.config.doc_settings import DocIngestionSettings

BASE_DIR = Path(__file__).resolve().parents[3]
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

settings = DocIngestionSettings()
docs_dir_path = settings.documents_path
vector_store_path = settings.vector_store_path
collection_name = settings.collection_name

def load_documents(data_path:str):
    documents = []

    for file in os.listdir(data_path):
        file_path = os.path.join(data_path, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif file.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf-8")
        else:
            continue

        documents.extend(loader.load())

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)


def get_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def load_vector_db():
    embeddings = get_embeddings()

    db = Chroma(
        persist_directory= str(vector_store_path),
        embedding_function=embeddings
    )

    return db
def create_vector_db(db_path:str):
    logger.info(f"loading documents from directory: {docs_dir_path}")
    docs = load_documents(str(docs_dir_path))
    if not docs:
        logger.warning("No documents found, skipping vector store build")
        return
    logger.info("create parser with chunking strategy")
    chunks = split_documents(docs)
    logger.info(f"parsed: {len(chunks)}")
    embeddings = get_embeddings()

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_path
    )
    logger.info("succesfully created chroma vector database store")




def build_vector_store_from_docs():
    logger.info("starting ingestion process")
    try:

        if not os.path.exists(vector_store_path):
            os.makedirs(vector_store_path)
        create_vector_db(str(vector_store_path))
        logger.info("Completed ingestion process")
    except Exception as e:
        logger.error(f"error during vector store build : {e}")

def ensure_vector_db():
    vectordb = load_vector_db()

    if vectordb._collection.count() == 0:
        print("⚠️ Vector DB empty → rebuilding...")
        build_vector_store_from_docs()

if __name__ == "__main__":
    build_vector_store_from_docs()
