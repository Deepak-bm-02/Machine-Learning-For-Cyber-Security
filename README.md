# Machine-Learning-For-Cyber-Security
README – Experiment 1
Title

Time Series Analysis of Historical Network Traffic Data

Objective

To analyze historical network traffic data using time series analysis techniques and identify trends, seasonality, and traffic patterns.

Dataset
File: output1.csv
Data Type: Historical Network Traffic
Main Feature: Timestamp
Tools Used
Python
Pandas
Matplotlib
Statsmodels
Workflow
Load the dataset.
Convert Unix timestamps to date-time format.
Sort data by timestamp.
Perform seasonal decomposition.
Visualize trend, seasonality, and residual components.
Output
Time series plot
Trend component
Seasonal component
Residual analysis
README – Experiment 2
Title

Predicting Potential DDoS Attacks Using ARIMA Time Series Forecasting

Objective

To forecast future DDoS attack patterns using the ARIMA model on the CICIDS2017 dataset.

Dataset
File: DDoS Attack Dataset.csv
Dataset: CICIDS2017
Target: DDoS Attack Prediction
Tools Used
Python
Pandas
Matplotlib
Statsmodels (ARIMA)
Workflow
Load the dataset.
Convert timestamps.
Create a binary attack column (BENIGN = 0, Attack = 1).
Aggregate attack counts by minute.
Split the data into training and testing sets.
Train the ARIMA model.
Forecast future attacks.
Compare actual and predicted values.
Evaluate the model using RMSE.
Output
Historical attack count graph
Forecast graph
Predicted attack values
RMSE evaluation metric
