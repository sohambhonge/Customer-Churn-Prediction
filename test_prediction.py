from churn_predictor import predict_customer

customer = {

    'SeniorCitizen': 0,
    'tenure': 12,
    'MonthlyCharges': 85,
    'TotalCharges': 1020,

    'gender_Male': 1,
    'Partner_Yes': 1,
    'Dependents_Yes': 0,

    'PhoneService_Yes': 1,

    'MultipleLines_No phone service': 0,
    'MultipleLines_Yes': 1,

    'InternetService_Fiber optic': 1,
    'InternetService_No': 0,

    'OnlineSecurity_No internet service': 0,
    'OnlineSecurity_Yes': 1,

    'OnlineBackup_No internet service': 0,
    'OnlineBackup_Yes': 1,

    'DeviceProtection_No internet service': 0,
    'DeviceProtection_Yes': 1,

    'TechSupport_No internet service': 0,
    'TechSupport_Yes': 0,

    'StreamingTV_No internet service': 0,
    'StreamingTV_Yes': 1,

    'StreamingMovies_No internet service': 0,
    'StreamingMovies_Yes': 1,

    'Contract_One year': 0,
    'Contract_Two year': 0,

    'PaperlessBilling_Yes': 1,

    'PaymentMethod_Credit card (automatic)': 0,
    'PaymentMethod_Electronic check': 1,
    'PaymentMethod_Mailed check': 0
}

prediction, probability = predict_customer(customer)

print("Prediction:", prediction)
print("Churn Probability:", round(probability * 100, 2), "%")