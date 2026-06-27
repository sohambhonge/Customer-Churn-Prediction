{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "dd8abf82-e42f-4d17-a224-7fa7e3ec21e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "from churn_predictor import predict_customer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c2297bf1-6479-43ba-a1d3-73778ebb9ff1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prediction: 0\n",
      "Probability: 0.1692745483615533\n"
     ]
    }
   ],
   "source": [
    "customer = {\n",
    "    'SeniorCitizen': 0,\n",
    "    'tenure': 12,\n",
    "    'MonthlyCharges': 85,\n",
    "    'TotalCharges': 1020\n",
    "}\n",
    "\n",
    "prediction, probability = predict_customer(customer)\n",
    "\n",
    "print(\"Prediction:\", prediction)\n",
    "print(\"Probability:\", probability)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb2fc2c2-824f-48b2-ab9a-9941ca18320e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "python (base)",
   "language": "python",
   "name": "base"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
