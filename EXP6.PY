import pandas as pd
import re
from sklearn.ensemble import IsolationForest

# Load dataset
data = pd.read_csv("malicious_phish.csv")

print("Dataset loaded successfully")
print("Original dataset shape:", data.shape)

# Select 10,000 URLs for analysis
data = data.sample(10000, random_state=42).copy()

# -------------------------------
# FEATURE ENGINEERING
# -------------------------------

# URL length
data["url_length"] = data["url"].apply(len)

# Number of dots
data["num_dots"] = data["url"].apply(
    lambda x: x.count(".")
)

# Number of hyphens
data["num_hyphens"] = data["url"].apply(
    lambda x: x.count("-")
)

# Number of digits
data["num_digits"] = data["url"].apply(
    lambda x: sum(c.isdigit() for c in x)
)

# Number of special characters
data["num_special"] = data["url"].apply(
    lambda x: len(re.findall(r"[^a-zA-Z0-9./-]", x))
)

# Number of subdirectories
data["num_subdirs"] = data["url"].apply(
    lambda x: x.count("/")
)

# -------------------------------
# SELECT FEATURES
# -------------------------------

X = data[
    [
        "url_length",
        "num_dots",
        "num_hyphens",
        "num_digits",
        "num_special",
        "num_subdirs"
    ]
]

# -------------------------------
# ISOLATION FOREST
# -------------------------------

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

# Train model and detect anomalies
prediction = model.fit_predict(X)

# Store prediction
data["result"] = prediction

# Convert values
data["result"] = data["result"].map({
    1: "Normal",
    -1: "Abnormal"
})

# -------------------------------
# DISPLAY RESULTS
# -------------------------------

print("\n-----------------------------")
print("URL ANOMALY DETECTION")
print("-----------------------------")

print("\nFirst 20 Results:")

print(
    data[
        [
            "url",
            "type",
            "url_length",
            "num_dots",
            "num_hyphens",
            "num_digits",
            "num_special",
            "num_subdirs",
            "result"
        ]
    ].head(20)
)

# Count normal and abnormal URLs
print("\nAnomaly Summary:")
print(data["result"].value_counts())

# Display abnormal URLs
print("\nAbnormal URLs:")

print(
    data[data["result"] == "Abnormal"][
        [
            "url",
            "type",
            "url_length",
            "num_dots",
            "num_hyphens",
            "num_digits",
            "num_special",
            "num_subdirs"
        ]
    ].head(10)
)