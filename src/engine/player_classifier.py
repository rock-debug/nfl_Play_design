import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from engine.features_player import extract_player_features

MODEL_PATH = "models/player_position_classifier.pkl"

POSITION_LABELS = [
    "QB","RB","FB","WR","TE",
    "LT","LG","C","RG","RT",
    "DE","DT","NT",
    "OLB","ILB","MLB","LB",
    "CB","S","FS","SS","NB"
]

class PlayerPositionClassifier:
    def __init__(self):
        self.model = None

    def load(self, path=MODEL_PATH):
        self.model = joblib.load(path)

    def save(self, path=MODEL_PATH):
        joblib.dump(self.model, path)

    def train(self, feature_list, label_list):
        """
        feature_list: [np.array(features)]
        label_list:   [role strings]
        """
        y = np.array([POSITION_LABELS.index(lbl) for lbl in label_list])
        X = np.stack(feature_list)
        self.model = RandomForestClassifier(
            n_estimators=200,
            max_depth=12,
            class_weight="balanced"
        )
        self.model.fit(X, y)
        print("Training complete.")

    def predict_role(self, route):
        """
        route: np.array(T,2)
        returns predicted role string
        """
        feat = extract_player_features(route)
        idx = self.model.predict(feat.reshape(1, -1))[0]
        return POSITION_LABELS[idx]

# global instance
classifier = PlayerPositionClassifier()

def load_classifier():
    classifier.load()
    return classifier

def predict_player_position(route):
    return classifier.predict_role(route)
