from environment.params import IMAGE_UPLOADED, LABELS_DICT_NUM_STR
from ml_logic.preprocess import preprocess
from ml_logic.registry import load_model
import numpy as np


async def predict() -> str:
    model = load_model()
    X_pred = preprocess(IMAGE_UPLOADED)
    img_pred = model.predict(X_pred)
    sample_pred = np.argmax(img_pred)
    predicted_fruit = LABELS_DICT_NUM_STR[sample_pred]
    return predicted_fruit
