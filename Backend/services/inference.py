import numpy as np

from .preprocessing import image_preprocessor
from ..models.classifer import Classifier
from PIL import Image
from .externalAPI import call_foodAPI

classes = ['Bean',
 'Bitter_Gourd',
 'Bottle_Gourd',
 'Brinjal',
 'Broccoli',
 'Cabbage',
 'Capsicum',
 'Carrot',
 'Cauliflower',
 'Cucumber',
 'Papaya',
 'Potato',
 'Pumpkin',
 'Radish',
 'Tomato']

CLASS_TO_API_NAME = {
    "Bean": "beans",
    "Bitter_Gourd": "bitter gourd",        
    "Bottle_Gourd": "bottle gourd",      
    "Brinjal": "eggplant",
    "Broccoli": "broccoli",
    "Cabbage": "cabbage",
    "Capsicum": "bell pepper",
    "Carrot": "carrot",
    "Cauliflower": "cauliflower",
    "Cucumber": "cucumber",
    "Papaya": "papaya",
    "Potato": "potato",
    "Pumpkin": "pumpkin",
    "Radish": "radish",
    "Tomato": "tomato"
}

path = 'Backend\model\cnn_model.h5'

model = Classifier(path)

def run_inference(image:Image.Image):
    converted_image = image_preprocessor(image)
    softmax_output = model.predict(converted_image)
    predicted_id = np.argmax(softmax_output,axis=1)[0]
    max_probability = np.max(softmax_output, axis=1)[0] * 100

    predicted_class = classes[predicted_id]
    print(predicted_class)
    print(max_probability)

    api_food_name = CLASS_TO_API_NAME.get(predicted_class, predicted_class)

    try:
        nutrients = call_foodAPI(api_food_name)
    except Exception as e:
        nutrients = None

    return predicted_class,max_probability,nutrients