
FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY ../../requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .. src/
COPY ../../doc_dir doc_dir/
COPY start.sh ./start.sh

RUN chmod +x start.sh

EXPOSE 8000 8501

ENV DOCUMENTS_DIR=doc_dir
ENV VECTOR_STORE_DIR=doc_vector_store
ENV COLLECTION_NAME=document_collection
ENV MODEL_NAME=gpt-4.1-2025-04-14
ENV MODEL_TEMPERATURE=0.0
ENV API_HOST=0.0.0.0
ENV API_PORT=8000

# 🔥 fixes
ENV CREWAI_DISABLE_TELEMETRY=true
ENV HOME=/tmp

# ⚠️ only OK if single-container setup
ENV BACKEND_URL=http://localhost:8000/

CMD ["/app/start.sh"]