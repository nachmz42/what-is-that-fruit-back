import numpy as np
from keras.preprocessing import image

def preprocess(image_path: str) -> np.array:
    new_image = image.load_img(image_path,target_size = (64,64))
    image_array = image.img_to_array(new_image)
    image_final = np.expand_dims(image_array ,axis=0)
    image_final /= 255.
    return image_final
