from typing import Any, Dict, Optional
from pydantic import BaseModel


class PredictionResponse(BaseModel):
    class_name: str
    confidence: float
    nutrition: Optional[Dict[str, Any]]
