import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib 

# load dataset
df: pd.DataFrame = pd.read_csv("datasets/Iris.csv")

# preprocessing
df.drop(columns="Id", axis=1, inplace=True)
encoder: LabelEncoder = LabelEncoder()
df['Species']= encoder.fit_transform(df['Species'])

# train test split
X: pd.DataFrame = df.drop(columns="Species", axis=1)
y: np.ndarray = df["Species"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train model
logistic: LogisticRegression = LogisticRegression(max_iter=200)
logistic.fit(X_train, y_train)

# uji model
y_pred: np.ndarray = logistic.predict(X_test)
acc: float = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.2f}")

# save model
joblib.dump(logistic, 'model.joblib')
joblib.dump(encoder, 'encoder.joblib')

