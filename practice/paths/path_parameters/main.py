from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

@app.get('/models/{model_name}')
async def get_model(model_name : ModelName):
    if model_name is ModelName.alexnet:
        return {'Model name': model_name, 'Message': 'Deep Learning FTW!' }

    if model_name.value == 'lenet':
        return {'Model name': model_name, 'Message': 'LeCNN all the images'}

    return {'Model name': model_name, 'Message': 'Have some residuals'}

