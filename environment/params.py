import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

LOCAL_DATA_PATH = os.getenv("LOCAL_DATA_PATH")
LOCAL_MODEL_PATH = os.getenv("LOCAL_MODEL_PATH")

IMAGE_UPLOAD_STORAGE = os.getenv("IMAGE_UPLOAD_STORAGE")
IMAGE_UPLOADED = os.getenv("IMAGE_UPLOADED")

LABELS_DICT_NUM_STR =  {
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
LABELS_DICT_STR_NUM = {
        'apple': 0,
        'banana': 1,
        'cherry':2,
        'chickoo':3,
        'grapes':4,
        'kiwi':5,
        'mango':6,
        'orange':7,
        'strawberry':8
    }

ABSOLUTE_LOCAL_DATA_PATH = os.getenv("ABSOLUTE_LOCAL_DATA_PATH")
