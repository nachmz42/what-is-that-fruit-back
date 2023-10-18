from pydantic import BaseModel


class FruitPredictionDto(BaseModel):
    prediction: str
