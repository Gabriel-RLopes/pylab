import pickle
from config import MODEL_PATH, VECTORIZER_PATH


class ModelManager:
    def load(self):
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        with open(VECTORIZER_PATH, 'rb') as f:
            vectorizer = pickle.load(f)
        return  model, vectorizer
