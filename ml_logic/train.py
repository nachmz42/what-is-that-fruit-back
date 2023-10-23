import numpy as np
import pathlib
from keras.utils import to_categorical
import cv2
from keras.models import Sequential
from keras.layers import Conv2D,Dense,Dropout, Flatten,MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
from colorama import Fore, Style

from environment.params import ABSOLUTE_LOCAL_DATA_PATH, LABELS_DICT_STR_NUM, LOCAL_DATA_PATH
from ml_logic.registry import save_model


def train():
    #Getting the paths to the data
    data_dir = pathlib.Path(LOCAL_DATA_PATH)
    fruit_images_dict = {
    'apple': list(data_dir.glob('apple fruit/*')),
    'banana': list(data_dir.glob('banana fruit/*')),
    'cherry':list(data_dir.glob('cherry fruit/*')),
    'chickoo':list(data_dir.glob('chickoo fruit/*')),
    'grapes':list(data_dir.glob('grapes fruit/*')),
    'kiwi':list(data_dir.glob('kiwi fruit/*')),
    'mango':list(data_dir.glob('mango fruit/*')),
    'orange':list(data_dir.glob('orange fruit/*')),
    'strawberry':list(data_dir.glob('strawberry fruit/*'))
    }

    IMAGE_WIDTH=64
    IMAGE_HEIGHT=64
    IMAGE_CHANNELS = 3
    X, Y = [], []
    #Transforming the files into X and Y
    for fruit_name, images in fruit_images_dict.items():
        for image in images:
            img = cv2.imread(str(image))
            if isinstance(img,type(None)):
                print('Image not found at' + str(image))
                continue

            elif ((img.shape[0] >= IMAGE_HEIGHT) and  (img.shape[1] >=IMAGE_WIDTH)):
                resized_img = cv2.resize(img,(IMAGE_WIDTH,IMAGE_HEIGHT))
                X.append(resized_img)
                Y.append(LABELS_DICT_STR_NUM[fruit_name])
            else:
                print("Invalid Image at " + str(image))
                continue

    X = np.array(X)
    Y = np.array(Y)


    #Transform Y into categorical
    Y = to_categorical(Y, num_classes=9)

    # Data agumentation
    datagen = ImageDataGenerator(rotation_range=10,
                rescale = 1./255,
                width_shift_range=0.1,
                height_shift_range=0.1,
                horizontal_flip=True,
                vertical_flip=False,
                zoom_range=0.1,
                shear_range=0.1,
                brightness_range=[0.8, 1.2],
                fill_mode='nearest',
                validation_split=0.2  # set validation split to 20%
                )

    # Import the data into train and Validation subset
    trainimagedata = datagen.flow_from_directory(ABSOLUTE_LOCAL_DATA_PATH,
                                                batch_size = 32,
                                                class_mode = 'categorical',
                                                target_size=(64,64),
                                                subset = 'training'
                                                )

    testimagedata = datagen.flow_from_directory(ABSOLUTE_LOCAL_DATA_PATH,
                                                batch_size = 32,
                                                class_mode = 'categorical',
                                                target_size=(64,64),
                                                subset = 'validation'
                                                )

    # Declare the model architecture

    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),

        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.25),
        Dense(128, activation='relu'),
        Dropout(0.25),
        Dense(9, activation='softmax')
    ])

    # Compile the model
    optimizer = Adam(lr=0.001,beta_1=0.9,beta_2 = 0.999, epsilon=1e-8)

    model.compile(optimizer = optimizer,
                loss = 'categorical_crossentropy',
                metrics = ['accuracy'])


    early_stop = EarlyStopping(monitor = 'val_loss', patience =15)
    print(Fore.BLUE + f"\nTraining the model..." + Style.RESET_ALL)
    # Fitting the model
    model.fit(trainimagedata,
                            validation_data = testimagedata,
                            epochs=35,
                            batch_size=16,
                            callbacks=[early_stop])
    print(Fore.BLUE + f"\Saving the model..." + Style.RESET_ALL)
    save_model(model)
    return None
