from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
