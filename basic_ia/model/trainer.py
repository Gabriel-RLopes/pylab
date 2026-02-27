import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from data.dataset import load_dataset
from config import MODEL_PATH, VECTORIZER_PATH


class Trainer:
    def train(self):
        texts, labels = load_dataset()
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(texts)

        model = MultinomialNB()
        model.fit(X, labels)

        with open(MODEL_PATH, 'wb') as f:
            pickle.dump(model, f)

        with open(VECTORIZER_PATH, 'wb') as f:
            pickle.dump(vectorizer, f)

        print('modelo treinado com sucesso')
