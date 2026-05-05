from dotenv import load_dotenv
from pathlib import Path

from langchain_community.vectorstores import Chroma
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[3]


load_dotenv()
class Settings(BaseSettings):
     """ Settings for backend
     """
     API_HOST: str = "localhost"
     API_PORT: int = 8000

     class Config:
          env_file =".env"
          env_file_encoding ="utf-8"
          extra ="allow"

     @property
     def get_api_port(self) -> int:
          return self.API_Port

     @property
     def get_api_host(self) -> str:
          return self.get_api_host



