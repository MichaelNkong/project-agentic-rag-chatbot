from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[3]



load_dotenv()
model_config = SettingsConfigDict(env_file=".env")
class DocIngestionSettings(BaseSettings):
     """ Settings for document ingestion
     """
     DOCUMENTS_DIR:str
     VECTOR_STORE_DIR:str
     COLLECTION_NAME: str

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

