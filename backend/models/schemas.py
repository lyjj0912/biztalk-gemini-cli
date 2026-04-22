from pydantic import BaseModel, Field

class ConvertRequest(BaseModel):
    text: str = Field(..., min_length=1)
    target_audience: str

class ConvertResponse(BaseModel):
    converted_text: str
    target_audience: str
    original_text: str
