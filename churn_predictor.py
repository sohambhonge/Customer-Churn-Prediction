import pandas as pd
import joblib

model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

def predict_customer(customer_data):

    df = pd.DataFrame([customer_data])

    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[feature_columns]

    scaled_data = scaler.transform(df)

    prediction = model.predict(scaled_data)[0]
    probability = model.predict_proba(scaled_data)[0][1]

    return prediction, probability