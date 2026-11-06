import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv(
    r"F:\MLCS\12th dataset\WSN-DS.csv"
)

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)
print("Columns:", data.columns.tolist())

# Remove missing values
data = data.dropna()

# Identify target column
target = 'Attack type'

# Separate input and output
X = data.drop(target, axis=1)
y = data[target]

# Convert categorical features
X = pd.get_dummies(X)

# Convert labels into Normal and Malicious
y = y.apply(
    lambda x: 0 if str(x).strip().lower() == 'normal' else 1
)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2,
    random_state=42, stratify=y
)

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train model
print("Training started...")
model.fit(X_train, y_train)

print("Training completed!")

# Prediction
pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, pred))

# Classification report
print(classification_report(y_test, pred))

# Test one network event
result = model.predict(X_test.iloc[[0]])

print("Network Event:",
      "Malicious" if result[0] == 1 else "Normal")