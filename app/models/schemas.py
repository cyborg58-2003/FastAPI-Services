from pydantic import BaseModel, Field

class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=10, description="The text to be summarized. Must be at least 10 characters long.")

class SummarizeResponse(BaseModel):
    original_length: int
    summary_length: int
    summary: str

class TranslateRequest(BaseModel):
    text: str = Field(..., min_length=1, description="The text to translate.")
    target_language: str = Field(..., min_length=2, description="The target language to translate the text into.")

class TranslateResponse(BaseModel):
    target_language: str
    translated_text: str

class GenerateEmailRequest(BaseModel):
    subject: str = Field(..., min_length=1, description="The subject of the email.")
    context: str = Field(..., min_length=1, description="The context or main points to include in the email body.")
    tone: str = Field("professional", description="The tone of the email (e.g., professional, casual).")

class GenerateEmailResponse(BaseModel):
    subject: str
    body: str
