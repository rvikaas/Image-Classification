
import numpy as np
from PIL import Image

image_size = (224,224)


def image_preprocessor(image:Image.Image):
    resized_image = image.resize(image_size)
    
    image_array = np.array(resized_image)

    normalized_image = image_array/255.0 #float64

    image_array = normalized_image.astype(np.float32)

    #adding a dimension for batch size (1,128,128,3)
    final_image = np.expand_dims(image_array,axis=0)

    return final_image

    
