from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.core.config import settings
from app.core.exceptions import validation_exception_handler, global_exception_handler
from app.api.endpoints import router as api_router
from app.core.logging_setup import logger

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        description="A REST API for text summarization, translation, and email generation.",
        version="1.0.0",
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Register Exception Handlers
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)

    # Include API Router
    app.include_router(api_router, prefix=settings.API_V1_STR)

    @app.on_event("startup")
    async def startup_event():
        logger.info(f"Starting {settings.APP_NAME}...")

    @app.get("/")
    def read_root():
        return {"message": f"Welcome to {settings.APP_NAME}. Visit /docs for API documentation."}

    return app

app = create_app()
