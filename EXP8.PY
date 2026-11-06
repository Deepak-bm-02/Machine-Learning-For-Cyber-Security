import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv(
    r"F:\MLCS\8th dataset\phishing_email.csv"
)

# Remove missing values
data = data.dropna(subset=['text_combined', 'label'])

# Use a smaller sample for faster training
data = data.sample(n=min(20000, len(data)), random_state=42)

# Input and output
X = data['text_combined'].astype(str)
y = data['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create optimized model
model = make_pipeline(
    TfidfVectorizer(max_features=1000, stop_words='english'),
    DecisionTreeClassifier(
        max_depth=15,
        min_samples_leaf=2,
        random_state=42
    )
)

print("Training started...")

# Train model
model.fit(X_train, y_train)

print("Training completed!")

# Prediction
pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, pred))

# Test new email
email = ["Your account is blocked. Click here immediately"]

result = model.predict(email)

print("Email Classification:", result[0])