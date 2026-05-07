import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.backend.config.backend_settings import Settings




logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:8501"] for Streamlit
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#app.include_router(chat_router)

settings = Settings()


#if __name__ == "__main__":
   # import uvicorn
   # uvicorn.run(
    #    "src.backend.main:app",
      #  host=settings.API_HOST,
     #   port=settings.API_PORT,
   # )
