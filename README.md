# REST API Application

A REST API application built with [FastAPI](https://fastapi.tiangolo.com/) that provides endpoints for text summarization, translation, and email generation. This project demonstrates Python fundamentals, clean API design, request validation, and error handling.

## Features

- **Summarization (`POST /api/v1/summarize`)**: Accepts text and returns a summary.
- **Translation (`POST /api/v1/translate`)**: Translates text into a target language.
- **Email Generation (`POST /api/v1/generate-email`)**: Generates an email body based on a subject, context, and tone.
- **Request Validation**: Automatic validation using Pydantic.
- **Error Handling**: Custom exception handlers for validation and unhandled errors.
- **Logging**: Structured logging configured throughout the app.
- **Environment Variables**: Managed using `pydantic-settings`.
- **API Documentation**: Interactive documentation provided automatically by FastAPI (Swagger UI and ReDoc).

## Project Structure

```
├── app/
│   ├── api/
│   │   └── endpoints.py      # API routing and endpoint definitions
│   ├── core/
│   │   ├── config.py         # Environment variables and settings
│   │   ├── exceptions.py     # Custom exception handlers
│   │   └── logging_setup.py  # Logging configuration
│   ├── models/
│   │   └── schemas.py        # Pydantic models for request/response
│   ├── services/
│   │   └── ai_service.py     # Core business logic (AI integration mock)
│   └── main.py               # FastAPI application entry point
├── .env.example              # Example environment variables file
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

### Prerequisites
- Python 3.9+

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <repository-directory>
```

### 2. Create and activate a virtual environment

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configuration

Copy the example environment file:

**Windows:**
```powershell
copy .env.example .env
```

**macOS/Linux:**
```bash
cp .env.example .env
```

Currently, the AI services are mocked. If you wish to use a real LLM API, you would populate `LLM_API_KEY` in the `.env` file and update `app/services/ai_service.py`.

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

## API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, you can access:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Deliverables Checklist

- [x] GitHub Repository initialized
- [x] README Documentation
- [x] API Documentation (via Swagger UI at `/docs`)
- [ ] Screen Recording Link (10–15 mins) - **To be completed by you**
