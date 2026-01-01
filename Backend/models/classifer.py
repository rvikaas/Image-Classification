from keras.models import load_model

class Classifier:
    def __init__(self,model_path):
        self.model = load_model(model_path)

    def predict(self, x):
        return self.model.predict(x)