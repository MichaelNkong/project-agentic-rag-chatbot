from dotenv import load_dotenv
from pathlib import Path

from langchain_community.vectorstores import Chroma
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.rag_doc_ingestion.ingest_docs import get_embeddings

BASE_DIR = Path(__file__).resolve().parents[3]


load_dotenv()
model_config = SettingsConfigDict(env_file=".env")
class AgentSettings(BaseSettings):
     """ Settings for document ingestion
     """
     DOCUMENTS_DIR:str
     VECTOR_STORE_DIR:str
     COLLECTION_NAME: str
     MODEL_NAME : str
     MODEL_TEMPERATURE:int
     OPENAI_API_KEY: str

     class Config:
          env_file =".env"
          env_file_encoding ="utf-8"
          extra ="allow"

     @property
     def documents_path(self) -> Path:
          return BASE_DIR / self.DOCUMENTS_DIR

     @property
     def vector_store_path(self) -> Path:
          return BASE_DIR / self.VECTOR_STORE_DIR

     @property
     def collection_name(self) -> str:
          return self.COLLECTION_NAME


     @property
     def model_name(self) -> str:
          return self.MODEL_NAME

     @property
     def model_temperature(self) -> int:
          return self.MODEL_TEMPERATURE

     @property
     def get_api_key(self) -> str:
          return self.OPENAI_API_KEY

     def load_vector_db(self):
          embeddings = get_embeddings()

          db = Chroma(
               persist_directory=str(BASE_DIR)+"/"+self.VECTOR_STORE_DIR,
               embedding_function=embeddings
          )

          return db
