# What is That Fruit? 🍎🍌🍊🍇

## Description

Little personal project to put into practice the skills acquired during the Le Wagon Data Science bootcamp. It's just a page where you can upload an image, and a CNN model (trained with Kaggle data) will detect which fruit it is.

## Installation

To get started, you need to create a `.env` file in the project directory with the following content:

````ini
IMAGE_UPLOAD_STORAGE = './image_storage'
IMAGE_UPLOADED = './image_storage/fruit_image.jpg'

LOCAL_MODEL_PATH = "./models/"
LOCAL_TRAINING_OUTPUTS_PATH = './models'
LOCAL_DATA_PATH = "../data/"
ABSOLUTE_LOCAL_DATA_PATH = "./data"

Please replace the values with the appropriate paths and configurations as needed.

## Usage

### Running the API

To start the API, use the following command:

```bash
make run_api

### Training the Model

If you want to train the model, follow these steps:

1. Make sure you have the necessary data in place. You can download the dataset from the following link: [Fruits Dataset Images](https://www.kaggle.com/datasets/shreyapmaher/fruits-dataset-images).

2. Place the dataset in the appropriate data directory.

3. Use the following command to train the model:

   ```bash
   make run_train

The training process will generate model files and save them in the specified model directory.
Now, your model is ready for fruit detection!

## Frontend Interface

For a user-friendly interface to interact with the API and perform fruit detection, you can check out the frontend project located in the following GitHub repository:

[What is That Fruit Frontend](https://github.com/nachmz42/what-is-that-fruit-front)

The frontend provides an intuitive way for users to upload images and receive fruit predictions using the API. You can follow the frontend project's README for installation and usage instructions.

Enjoy using the frontend interface for fruit detection!
````
