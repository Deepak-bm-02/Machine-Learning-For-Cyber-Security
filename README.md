# Cybersecurity and Machine Learning Experiments

This repository contains 12 practical experiments based on Machine Learning, Time Series Analysis, and Cybersecurity using Python. These experiments focus on network traffic analysis, cyber-attack detection, URL classification, email security, CAPTCHA image analysis, and database security.

## Experiments

### Experiment 1: Time Series Decomposition

**Aim:** To decompose a time series dataset into trend, seasonal, and residual components.

**Methods Used:**
- Time Series Decomposition
- Trend Analysis
- Seasonal Analysis

**Tools:** Python, Pandas, Matplotlib, Statsmodels

**Result:** The time series data was decomposed into trend, seasonal, and residual components.

---

### Experiment 2: DDoS Attack Prediction Using Time Series Forecasting

**Aim:** To analyze historical network traffic and forecast potential DDoS attack periods.

**Methods Used:**
- Time Series Analysis
- ARIMA Forecasting
- Network Traffic Analysis

**Tools:** Python, Pandas, Matplotlib, Statsmodels

**Result:** Network traffic was forecasted, and abnormal traffic spikes were identified as potential DDoS attack periods.

---

### Experiment 3: Cyber-Attack Classification Using Ensemble Learning

**Aim:** To classify network traffic as Normal or Cyber-Attack using Random Forest.

**Dataset:** UNSW-NB15 Network Intrusion Dataset (Kaggle).

**Methods Used:**
- Data Preprocessing
- Categorical Feature Encoding
- Random Forest Classification
- Ensemble Learning
- Classification Evaluation

**Tools:** Python, Pandas, NumPy, Scikit-learn

**Result:** A Random Forest model was implemented to classify network traffic into Normal and Cyber-Attack categories.

---

### Experiment 4: Malicious URL Classification Using Logistic Regression

**Aim:** To classify URLs as legitimate or malicious using Logistic Regression.

**Dataset:** URL classification dataset containing legitimate and malicious URLs.

**Methods Used:**
- Data Preprocessing
- Feature Extraction
- Logistic Regression
- Classification Evaluation

**Tools:** Python, Pandas, Scikit-learn

**Result:** A Logistic Regression model was implemented to classify URLs into legitimate and malicious categories.

---

### Experiment 5: URL Classification Using Support Vector Machine (SVM)

**Aim:** To apply a Support Vector Machine (SVM) algorithm to classify URLs into legitimate and malicious categories.

**Dataset:** URL dataset containing legitimate and malicious URLs.

**Methods Used:**
- URL Data Preprocessing
- Feature Extraction
- Support Vector Machine Classification
- Classification Evaluation

**Tools:** Python, Pandas, NumPy, Scikit-learn

**Result:** An SVM model was implemented to classify URLs as legitimate or malicious.

---

### Experiment 6: Abnormal URL Pattern Detection Using Feature Engineering

**Aim:** To use a set of URLs and detect abnormal patterns through feature engineering.

**Dataset:** A collection of URLs containing normal and potentially abnormal patterns.

**Methods Used:**
- URL Analysis
- Feature Engineering
- URL Feature Extraction
- Abnormal Pattern Detection

**Tools:** Python, Pandas, NumPy, Scikit-learn

**Result:** URL features were extracted and analyzed to identify abnormal URL patterns.

---

### Experiment 7: CAPTCHA Image Analysis Using K-Means

**Aim:** To analyze CAPTCHA images and group them based on visual features using K-Means clustering.

**Dataset:** CAPTCHA Image Dataset (Kaggle), with 719 images processed.

**Methods Used:**
- Image Preprocessing
- Contrast Extraction
- Edge Detection
- Brightness Analysis
- K-Means Clustering

**Tools:** Python, OpenCV, NumPy, Scikit-learn

**Result:** The model processed 719 images and grouped them into two clusters:
- Cluster 0: 396 images
- Cluster 1: 323 images

---

### Experiment 8: Email Spoofing Pattern Detection Using Machine Learning

**Aim:** To identify suspicious email patterns and classify emails as legitimate or phishing using a Decision Tree Classifier.

**Dataset:** Phishing Email Dataset (Kaggle).

**Methods Used:**
- Data Preprocessing
- TF-IDF Feature Extraction
- Decision Tree Classification
- Classification Evaluation

**Tools:** Python, Pandas, Scikit-learn

**Result:** The Decision Tree model classified email content and achieved 89.75% accuracy on the selected test split.

---

### Experiment 9: Email Spam Classification Using Naive Bayes

**Aim:** To classify emails as Spam or Not Spam using the Naive Bayes algorithm.

**Dataset:** Email Spam Classification Dataset (Kaggle), containing 5,172 email records.

**Methods Used:**
- Data Preprocessing
- Feature Selection
- Multinomial Naive Bayes
- Classification Evaluation

**Tools:** Python, Pandas, Scikit-learn

**Result:** A Naive Bayes model was implemented to classify emails into spam and legitimate categories.

---

### Experiment 10: Network Anomaly Detection Using K-Means

**Aim:** To detect abnormal network activities by grouping network traffic using K-Means clustering.

**Dataset:** NSL-KDD Network Intrusion Dataset (Kaggle).

**Methods Used:**
- Data Preprocessing
- Feature Scaling
- K-Means Clustering
- Network Anomaly Detection

**Tools:** Python, Pandas, NumPy, Scikit-learn

**Result:** The K-Means model was implemented to group network events into clusters for anomaly analysis.

---

### Experiment 11: Malicious Data Injection Detection in Databases Using Decision Tree

**Aim:** To detect malicious SQL injection queries using a Decision Tree Classifier.

**Dataset:** SQL Injection Dataset (Kaggle).

**Methods Used:**
- Text Preprocessing
- TF-IDF Feature Extraction
- Decision Tree Classification
- SQL Injection Detection

**Tools:** Python, Pandas, Scikit-learn

**Result:** The Decision Tree model was implemented to identify suspicious SQL queries and classify them as Normal or Malicious.

---

### Experiment 12: Malicious Event Detection in Wireless Sensor Networks

**Aim:** To detect malicious activities in Wireless Sensor Networks using network features and a Decision Tree Classifier.

**Dataset:** WSN-DS Dataset (Kaggle).

**Methods Used:**
- Data Preprocessing
- Feature Selection
- Decision Tree Classification
- Network Intrusion Detection

**Tools:** Python, Pandas, Scikit-learn

**Result:** The Decision Tree model was implemented to classify wireless sensor network events as Normal or Malicious.

---

## Installation

Install the required Python libraries:

```bash
pip install pandas numpy scikit-learn opencv-python matplotlib statsmodels
```

## How to Run

1. Download the required datasets.
2. Extract each dataset into its respective folder.
3. Open the Python programs in VS Code.
4. Install the required libraries.
5. Update dataset file paths if necessary.
6. Run the Python programs.
7. Observe the output and model performance.

Example:

```bash
python EXP1.py
```

## Project Objectives

- Analyze time series data and network traffic.
- Forecast potential DDoS attack periods.
- Classify normal and malicious network traffic.
- Detect malicious and legitimate URLs.
- Identify abnormal URL patterns using feature engineering.
- Analyze CAPTCHA image characteristics.
- Identify suspicious and phishing emails.
- Classify spam and legitimate emails.
- Detect abnormal network activities.
- Identify malicious SQL injection queries.
- Detect attacks in wireless sensor networks.

## Conclusion

These experiments demonstrate the practical applications of Machine Learning and Time Series Analysis in cybersecurity. Algorithms such as Naive Bayes, K-Means, Logistic Regression, Support Vector Machine, Decision Tree, Random Forest, and ARIMA are used to analyze data, detect suspicious activities, forecast network traffic, and classify potential cyber threats using Python.
