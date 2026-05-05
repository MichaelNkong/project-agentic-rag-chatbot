FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ src/
COPY doc_dir/ doc_dir/
COPY start.sh ./start.sh

# Make start.sh executable
RUN chmod +x start.sh

# Expose backend and frontend ports
EXPOSE 8000 8501

# Set environment variables (can be overridden at runtime)
ENV DOCUMENTS_DIR=doc_dir
ENV VECTOR_STORE_DIR=doc_vector_store
ENV COLLECTION_NAME=document_collection
ENV MODEL_NAME=gpt-4.1-2025-04-14
ENV MODEL_TEMPERATURE=0.0
ENV API_HOST=0.0.0.0
ENV API_PORT=8000
ENV CREWAI_DISABLE_TELEMETRY=true
ENV BACKEND_URL=http://localhost:8000/


# Run all services using start.sh
CMD ["/app/start.sh"]
