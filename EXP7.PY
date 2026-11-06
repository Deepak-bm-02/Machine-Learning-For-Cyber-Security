import cv2
import glob
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load CAPTCHA images
files = glob.glob(r"F:\MLCS\7th dataset\*.jpg")

print("Images found:", len(files))

features = []

# Extract image features
for file in files:

    img = cv2.imread(file, 0)

    if img is None:
        continue

    contrast = np.std(img)

    edges = cv2.Canny(img, 100, 200)

    edge_density = np.mean(edges > 0)

    brightness = np.mean(img)

    features.append([
        contrast,
        edge_density,
        brightness
    ])

# Convert into array
X = np.array(features)

# Check data
if len(X) < 2:
    print("Not enough images found!")
    exit()

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means clustering
model = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

labels = model.fit_predict(X_scaled)

# Display results
print("\nCAPTCHA Analysis Completed!")

print("Total images:", len(X))

for i in range(2):
    print("Cluster", i, "Images:", np.sum(labels == i))