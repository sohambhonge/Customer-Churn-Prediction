# Customer Churn Prediction

## Project Overview

This project predicts customer churn for a telecommunications company using Machine Learning. The objective is to identify customers who are likely to discontinue services based on demographic information, account details, and service usage patterns.

## Dataset

- Dataset: Telco Customer Churn Dataset
- Source: Kaggle
- Link: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

The dataset contains customer information such as tenure, contract type, internet service, billing details, payment methods, and churn status.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Jupyter Notebook

## Project Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Feature Scaling
6. Model Training
7. Model Evaluation
8. Model Persistence
9. Customer Churn Prediction

## Model

Algorithm Used:

- Logistic Regression

Evaluation Metrics:

- Accuracy Score
- Confusion Matrix
- Classification Report

## Project Structure

```text
Customer-Churn-Prediction/
│
├── Customer Churn Prediction.ipynb
├── Telco Customer Churn.csv
│
├── churn_model.pkl
├── scaler.pkl
├── feature_columns.pkl
│
├── churn_predictor.py
├── predict_new_customer.py
│
└── README.md
```

## Model Saving

The trained model and preprocessing artifacts are saved using Joblib.

```python
joblib.dump(model, "churn_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(list(X.columns), "feature_columns.pkl")
```

## Prediction Example

```python
from churn_predictor import predict_customer

customer = {
    'SeniorCitizen': 0,
    'tenure': 12,
    'MonthlyCharges': 85,
    'TotalCharges': 1020
}

prediction, probability = predict_customer(customer)

print("Prediction:", prediction)
print("Probability:", probability)
```

## Results

- Built an end-to-end customer churn prediction pipeline.
- Performed data preprocessing and feature engineering.
- Trained and evaluated a Logistic Regression model.
- Generated churn probability predictions for new customers.
- Created a reusable prediction module for future predictions.

## Future Enhancements

- Random Forest Classifier
- XGBoost
- Hyperparameter Tuning
- Model Deployment using Flask/FastAPI
- Interactive Dashboard Integration
