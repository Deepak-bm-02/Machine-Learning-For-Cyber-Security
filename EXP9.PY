import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv(r"F:\MLCS\9th dataset\emails.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)

# Remove text column if present
data = data.drop(columns=['Email'], errors='ignore')

# Separate input and output
X = data.drop('Prediction', axis=1)
y = data['Prediction']

# Keep numerical features only
X = X.select_dtypes(include='number')

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create Naive Bayes model
model = MultinomialNB()

# Train model
model.fit(X_train, y_train)

print("Training completed!")

# Prediction
pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, pred))

# Classification report
print(classification_report(y_test, pred))

# Test an email
result = model.predict(X_test.iloc[[0]])

print("Email Classification:",
      "Spam" if result[0] == 1 else "Not Spam")