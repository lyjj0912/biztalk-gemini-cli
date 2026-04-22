from fastapi import APIRouter, HTTPException
from models.schemas import ConvertRequest, ConvertResponse
from services.tone_converter import ToneConverter

router = APIRouter()
converter = ToneConverter()

@router.post("/convert", response_model=ConvertResponse)
async def convert_tone(request: ConvertRequest):
    try:
        converted = await converter.convert(request.text, request.target_audience)
        return ConvertResponse(
            converted_text=converted,
            target_audience=request.target_audience,
            original_text=request.text
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
