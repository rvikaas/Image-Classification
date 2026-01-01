import numpy as np

from .preprocessing import image_preprocessor
from ..models.classifer import Classifier
from PIL import Image

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

path = 'Backend\model\cnn_model.h5'

model = Classifier(path)

def run_inference(image:Image.Image):
    converted_image = image_preprocessor(image)
    softmax_output = model.predict(converted_image)

    predicted_id = np.argmax(softmax_output,axis=1)[0]
    max_probability = np.max(softmax_output, axis=1)[0] * 100

    predicted_class = classes[predicted_id]


    return predicted_class,max_probability