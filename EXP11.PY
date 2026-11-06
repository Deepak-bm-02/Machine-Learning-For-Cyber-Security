import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv(
    r"F:\MLCS\11th dataset\Modified_SQL_Dataset.csv"
)

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)
print("Columns:", data.columns.tolist())

# Select input and output
X = data['Query'].fillna('').astype(str)
y = data['Label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create Decision Tree model
model = make_pipeline(
    TfidfVectorizer(max_features=3000),
    DecisionTreeClassifier(
        max_depth=15,
        random_state=42
    )
)

# Train model
print("Training started...")
model.fit(X_train, y_train)

print("Training completed!")

# Prediction
pred = model.predict(X_test)

# Display accuracy
print("Accuracy:", accuracy_score(y_test, pred))

# Classification report
print(classification_report(y_test, pred))

# Test a new SQL query
query = ["SELECT * FROM users WHERE id=1 OR 1=1"]

result = model.predict(query)

print("SQL Query Classification:", result[0])