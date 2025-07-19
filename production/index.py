import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib

def iris_prediction(features: list[float]) -> str:
    """
    Predict the species of an iris flower based on its features.

    Parameters:
    features (list[float]): A list containing the features of the iris flower in the order:
                            [SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]

    Returns:
    str: The predicted species of the iris flower.
    """
    # Load pre-trained model and label encoder
    model: LogisticRegression = joblib.load("model.joblib")
    label_encoder: LabelEncoder = joblib.load("encoder.joblib")

    # Create DataFrame for the input features
    feature_names: list[str] = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
    input_data = pd.DataFrame([features], columns=feature_names)

    # Predict species
    prediction: np.ndarray = model.predict(input_data)

    # Convert numerical prediction to species label
    species: str = label_encoder.inverse_transform(prediction)[0]

    return species

if __name__ == "__main__":
    sample_input: list[float] = [3.0, 3.0, 2.0, 2.5]
    predicted_species: str = iris_prediction(sample_input)
    print(f"Predicted Species: {predicted_species}")