import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train():
    data = {
        "temp": [30, 25, 20, 15, 35],
        "humidity": [80, 60, 50, 40, 90],
        "wind": [10, 5, 7, 3, 12],
        "rain": [1, 0, 0, 0, 1]
    }

    df = pd.DataFrame(data)

    X = df[["temp", "humidity", "wind"]]
    y = df["rain"]

    model = RandomForestClassifier()
    model.fit(X, y)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/weather_model.pkl")

    print("Weather model trained successfully!")

if __name__ == "__main__":
    train()