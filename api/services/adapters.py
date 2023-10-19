


from api.model.fruit_prediction_dto import FruitPredictionDto


def predictionToPredictionDto(pred: str)-> FruitPredictionDto:
    '''
    Converts the prediction string to FruitPredictionDto
    '''
    return FruitPredictionDto(prediction=pred)
