import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
data = pd.read_csv("phishing_features.csv")

# Display dataset information
print("Dataset loaded successfully")
print("Dataset shape:", data.shape)

# Select features
X = data[
    [
        "url_length",
        "num_dots",
        "has_https",
        "has_ip",
        "suspicious_words",
        "digits_count"
    ]
]

# Target column
y = data["label"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create SVM model
svm_model = SVC(kernel="linear")

# Train the model
svm_model.fit(X_train, y_train)

# Predict test data
y_pred = svm_model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display results
print("\n-----------------------------")
print("SVM URL CLASSIFICATION")
print("-----------------------------")

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("Accuracy:", accuracy)

# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification completed successfully.")