import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the trained model
loaded_model = joblib.load('S5_humid_RFR_model.pkl')

# Load your validation data
validation_data = pd.read_csv('S5_edited.csv', usecols=[1, 3, 5, 7, 9])

# Extract features and actual target values
X_validation = validation_data[[
    'S1 Humidity (%)', 'S2 Humidity (%)', 'S3 Humidity (%)', 'S4 Humidity (%)']]
y_validation = validation_data['S5 Humidity (%)']

# Make predictions on the validation dataset
validation_predictions = loaded_model.predict(X_validation)

# Create a scatter plot to compare actual vs. predicted values with 'orange' and 'red' colors
colors = ['orange' if x < y else 'red' for x,
          y in zip(y_validation, validation_predictions)]

plt.figure(figsize=(8, 6))
plt.scatter(y_validation, validation_predictions, alpha=0.5, c=colors)
plt.xlabel('Actual S5 Humidity (%)')
plt.ylabel('Predicted S5 Humidity (%)')
plt.title('Actual vs. Predicted S5 Humidity (%)')
plt.show()
