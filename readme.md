# PharmaSync: High-Throughput Clinical Document Pipeline

## Project Overview
PharmaSync is an asynchronous, event-driven microservice designed to ingest, validate, and extract intelligence from unstructured Clinical Trial regulatory documents (PDFs).

Unlike traditional synchronous scripts, PharmaSync leverages a non-blocking architecture to handle high-volume ingestion queues, mirroring the reliability standards required in HealthTech & Life Sciences.

## Architecture
- **API Layer**: FastAPI (Async/Await)
- **Validation**: Pydantic (Strict Schema Enforcement)
- **Task Queue**: Celery + Redis (Background Processing)
- **Persistence**: PostgreSQL (Structured Metadata)
- **Extraction**: PDFPlumber + Regex (OCR & Text Mining)

## Setup
1. Clone the repo
2. `pip install -r requirements.txt`
3. `docker-compose up -d` (Redis & DB)
4. `uvicorn app.main:app --reload`