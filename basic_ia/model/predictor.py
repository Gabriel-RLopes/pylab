from model.model_manager import ModelManager


class Predictor:

    def __init__(self):
        self.model, self.vectorizer = ModelManager().load()

    def predict(self, text):
        X = self.vectorizer.transform([text])
        prediction = self.model.predict(X)
        return prediction[0]

