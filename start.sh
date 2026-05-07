#!/bin/bash
set -e

#python -m src.rag_doc_ingestion.ingest_docs

python -m src.backend.main --host 0.0.0.0 --port $PORT

#streamlit run src/frontend/app.py --server.port 8501 --server.address 0.0.0.0