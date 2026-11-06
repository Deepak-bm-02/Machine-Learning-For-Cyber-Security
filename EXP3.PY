import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load training dataset
train = pd.read_csv(
    r"F:\MLCS\3rd dataset\UNSW_NB15_training-set.csv"
)

# Load testing dataset
test = pd.read_csv(
    r"F:\MLCS\3rd dataset\UNSW_NB15_testing-set.csv"
)

print("Dataset loaded successfully!")

# Separate input and output
X_train = train.drop(
    columns=['label', 'attack_cat', 'id'],
    errors='ignore'
)

y_train = train['label']

X_test = test.drop(
    columns=['label', 'attack_cat', 'id'],
    errors='ignore'
)

y_test = test['label']

# Convert categorical features
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

# Match columns
X_test = X_test.reindex(
    columns=X_train.columns,
    fill_value=0
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Train model
print("Training started...")
model.fit(X_train, y_train)

print("Training completed!")

# Predict
pred = model.predict(X_test)

# Calculate accuracy
print("Accuracy:", accuracy_score(y_test, pred))

# Classification report
print(classification_report(y_test, pred))

# Test one network event
result = model.predict(X_test.iloc[[0]])

print("Network Status:",
      "Cyber Attack" if result[0] == 1 else "Normal")