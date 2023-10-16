from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import os

# from api.model.FruitDto import FruitDto
# from api.model.FruitPredictionDto import FruitPredictionDto

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

# @app.post('/predict/fruit')
# async def predictStroke(fruit_dto: FruitDto) -> FruitPredictionDto | None:
#     print("This is the API")
#     print("This is the API")
#     print("This is the API")
#     print("This is the API")
#     print("This is the API")
#     print("This is the API")

#     return FruitPredictionDto()

@app.post('/predict/fruit')
async def predict_fruits(file: UploadFile) ->  None:
    if file:
        # Guarda la imagen en una ruta local
        file_path = os.path.join(os.path.abspath('./what-is-that-fruit-back/imagenes_prueba'), file.filename)
        with open(file_path, "wb") as image_file:
            image_file.write(file.file.read())
        return None
    else:
        return None
