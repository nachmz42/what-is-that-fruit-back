from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from api.model.fruit_prediction_dto import FruitPredictionDto
from api.services.adapters import predictionToPredictionDto
from ml_logic.predict import predict


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get('/')
def index() -> dict:
    return {'ok': True}

@app.post('/predict/fruit')
async def predict_fruits(file: UploadFile) -> FruitPredictionDto | None:
    if file:
        pred = predict(file)
        response = predictionToPredictionDto(pred)
        return response
    else:
        return None
