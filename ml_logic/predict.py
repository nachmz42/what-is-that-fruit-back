from ml_logic.preprocess import preprocess
from ml_logic.registry import load_model
import numpy as np


async def predict() -> str:
    image_dir = '/home/nachmz42/code/nachmz42/what-is-that-fruit-back/imagenes_prueba/fruit_image.jpg'
    model = load_model()
    X_pred = preprocess(image_dir)
    img_pred = model.predict(X_pred)
    sample_pred = np.argmax(img_pred)

    # Map the number of the class with the name of the fruit
    fruit_labels_dict = {
        0: 'Apple',
        1: 'Banana',
        2: 'Cherry',
        3: 'Chickoo',
        4: 'Grapes',
        5: 'Kiwi',
        6: 'Mango',
        7: 'Orange',
        8: 'Strawberry'
    }

    predicted_fruit = fruit_labels_dict[sample_pred]
    return predicted_fruit
