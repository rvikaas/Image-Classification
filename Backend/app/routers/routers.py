from fastapi import APIRouter, File, UploadFile
from PIL import Image

from Backend.schemas.response import PredictionResponse
from Backend.services.inference import run_inference


router = APIRouter()

@router.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    
    image = Image.open(file.file).convert('RGB')

    #Run inference
    predicted_class,probabilty = run_inference(image)

    return PredictionResponse(
        class_name = predicted_class,
        confidence = probabilty
        )


