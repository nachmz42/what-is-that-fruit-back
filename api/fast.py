from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from api.model.fruit_prediction_dto import FruitPredictionDto
from api.services.adapters import predictionToPredictionDto
from environment.params import IMAGE_UPLOAD_STORAGE
from ml_logic.predict import predict
import os

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

@app.post('/upload')
async def upload(file: UploadFile) -> None:
    if file:
        file_extension = os.path.splitext(file.filename)[1]
        unique_filename = f"fruit_image{file_extension}"

        destination_directory = os.path.abspath(IMAGE_UPLOAD_STORAGE)
        os.makedirs(destination_directory, exist_ok=True)
        file_path = os.path.join(os.path.abspath(destination_directory), unique_filename)
        with open(file_path, "wb") as image_file:
            image_file.write(file.file.read())
        return None
    else:
        return None

@app.get('/predict')
async def predict_fruit() -> FruitPredictionDto:
        pred = await predict()
        response = predictionToPredictionDto(pred)
        return response
