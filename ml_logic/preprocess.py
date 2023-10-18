from keras.preprocessing import image
import numpy as np
from fastapi import UploadFile
from io import BytesIO
from PIL import Image

def preprocess(image_file: UploadFile) -> np.array:

    image_data = image_file.file.read()
    image = Image.open(BytesIO(image_data))
    image = image.resize((64, 64))
    image_array = np.array(image)
    image_final = np.expand_dims(image_array ,axis=0)
    image_final = (image_final * 255).astype(np.uint8)

    return image_final
