import logging
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from src.backend.config.backend_settings import Settings
from src.backend.services.chat import get_answer

logger = logging.getLogger(__name__)
print("MAIN FILE STARTING")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

app = FastAPI()
print("IMPORTING ROUTER")
print("ROUTER INCLUDED")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:8501"] for Streamlit
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


settings = Settings()
class ChatMessage(BaseModel):
    role: str
    content: str

class ChatHistoryRequest(BaseModel):
    chat_history: List[ChatMessage]


@app.post("/chat/answer")
async def chat_answer(request: ChatHistoryRequest):
    logger.info(f"Received API request with chat_history: {request.chat_history}")
    try:
        chat_history = [msg.dict() for msg in request.chat_history]
        result = get_answer(chat_history)
        logger.info(f"API response: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in chat_answer: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

#if __name__ == "__main__":
   # import uvicorn
   # uvicorn.run(
    #    "src.backend.main:app",
      #  host=settings.API_HOST,
     #   port=settings.API_PORT,
   # )
