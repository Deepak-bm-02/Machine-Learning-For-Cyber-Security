import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("dataNN.csv")

# Separate URL and label
X = data["url"].astype(str)
y = data["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training data:", len(X_train))
print("Testing data:", len(X_test))

# Convert URLs into numerical features
vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(2, 4),
    max_features=50000
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print("Feature extraction completed.")

# Create Logistic Regression model
model = LogisticRegression(
    max_iter=500,
    class_weight="balanced"
)

# Train model
print("Training model...")
model.fit(X_train, y_train)

print("Training completed.")

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# Classification report
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Legitimate", "Malicious"]
))