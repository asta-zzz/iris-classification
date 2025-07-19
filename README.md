<h1 align="center">IRIS CLASSIFICATION🌸</h1>

---

### Description 📄

Iris Classification is a simple prediction project used to determine the type of Iris flower based on four main features: `SepalLengthCm`, `SepalWidthCm`, `PetalLengthCm`, dan `PetalWidthCm`.

By simply entering the values of these four features, the model will predict the classification of the Iris flower, whether it belongs to Setosa, Versicolor, or Virginica.

---

### Datasets 📁

The dataset used can be downloaded directly from Kaggle:
🔗 <a href="https://www.kaggle.com/datasets/uciml/iris">Iris Species Dataset - Kaggle</a>

Make sure the CSV file (`Iris.csv`) is saved in the `datasets/` folder so that the script can run immediately.

---

### Dependencies & Setup 📦

##### 1. Clone Repository

```bash
git clone https://github.com/asta-zzz/iris-classification.git
```

```bash
cd iris-classification
```

##### 2. Create virtual environment

```bash
python -m venv venv
```

To activate it. <br>
Windows

```bash
venv\Scripts\activate
```

or <br>
Linux, Mac, GitBash

```bash
source venv/Scripts/activate
```

##### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### Model Accuracy 📈

Model accuracy on testing dataset: **100%**

---

### Folder Structure 📂

```pgsql
.
├── datasets/
├── production/
│   ├── index.py
│   └── model.py
├── model.joblib
├── encoder.joblib
├── requirements.txt
└── README.md

```

---

### Prediction Result 🧠

```vbnet
input: [3.0, 3.0, 2.0, 2.5]
output: Predicted Species: Iris-setosa
```
