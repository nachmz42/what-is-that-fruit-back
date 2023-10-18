import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

LOCAL_DATA_PATH = os.path.join("data/")
LABELS_DICT = {
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

LOCAL_TRAINING_OUTPUTS_PATH = os.path.join('.models')
