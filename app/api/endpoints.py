from fastapi import APIRouter, HTTPException
from app.models.schemas import (
    SummarizeRequest, SummarizeResponse,
    TranslateRequest, TranslateResponse,
    GenerateEmailRequest, GenerateEmailResponse
)
from app.services.ai_service import AIService
from app.core.logging_setup import logger

router = APIRouter()

@router.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    """
    Summarize the provided text.
    """
    try:
        summary = await AIService.summarize_text(request.text)
        return SummarizeResponse(
            original_length=len(request.text),
            summary_length=len(summary),
            summary=summary
        )
    except Exception as e:
        logger.error(f"Error in summarize endpoint: {e}")
        raise HTTPException(status_code=500, detail="Failed to summarize text.")

@router.post("/translate", response_model=TranslateResponse)
async def translate(request: TranslateRequest):
    """
    Translate text into the specified target language.
    """
    try:
        translated = await AIService.translate_text(request.text, request.target_language)
        return TranslateResponse(
            target_language=request.target_language,
            translated_text=translated
        )
    except Exception as e:
        logger.error(f"Error in translate endpoint: {e}")
        raise HTTPException(status_code=500, detail="Failed to translate text.")

@router.post("/generate-email", response_model=GenerateEmailResponse)
async def generate_email(request: GenerateEmailRequest):
    """
    Generate an email body based on the provided subject, context, and tone.
    """
    try:
        body = await AIService.generate_email(request.subject, request.context, request.tone)
        return GenerateEmailResponse(
            subject=request.subject,
            body=body
        )
    except Exception as e:
        logger.error(f"Error in generate-email endpoint: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate email.")
