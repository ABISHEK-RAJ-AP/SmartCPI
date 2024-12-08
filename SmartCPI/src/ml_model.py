from sklearn.ensemble import RandomForestRegressor
import pickle

class MLModel:
    def __init__(self):
        try:
            with open('model.pkl', 'rb') as model_file:
                self.model = pickle.load(model_file)
        except FileNotFoundError:
            self.model = RandomForestRegressor()
            # Placeholder for model training logic
            # self.train_model()

    def predict(self, features):
        return self.model.predict([features])[0]

    def train_model(self, features, targets):
        self.model.fit(features, targets)
        with open('model.pkl', 'wb') as model_file:
            pickle.dump(self.model, model_file)