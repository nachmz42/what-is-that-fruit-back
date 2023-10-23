from colorama import Fore, Style
import glob
import os
import pickle
import time
from keras.models import Sequential

from environment.params import LOCAL_MODEL_PATH




def save_model(model: Sequential) -> None:
    timestamp = time.strftime("%Y%m%d-%H%M%S")  # e.g. 20210824-154952

    # Save Model locally
    model_path =  LOCAL_MODEL_PATH + f"{timestamp}.pkl"
    pickle.dump(model, open(model_path, 'wb'))

    print("✅ Model saved locally")

    return None

def load_model() -> Sequential:
    #load model locally
    local_model_paths = glob.glob(f"{LOCAL_MODEL_PATH}*")
    if not local_model_paths:
        print(Fore.YELLOW +
                f"⚠️ No model found in {LOCAL_MODEL_PATH}"
                + Style.RESET_ALL)
        raise FileNotFoundError

    most_recent_model_path_on_disk = sorted(
        local_model_paths)[-1]

    print(f"✅ Model found at {most_recent_model_path_on_disk}")
    print(Fore.BLUE + f"\nLoad latest model from disk..." + Style.RESET_ALL)

    latest_model = pickle.load(
        open(most_recent_model_path_on_disk, "rb"))

    print("✅ Model loaded from local disk")

    return latest_model
