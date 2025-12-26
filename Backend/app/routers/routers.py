from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    pass