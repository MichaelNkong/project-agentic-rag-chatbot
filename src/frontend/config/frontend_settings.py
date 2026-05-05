from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    BACKEND_URL: str = "http://localhost:8000/"

    class Config:
        env_file = ".env"
        extra="allow"
