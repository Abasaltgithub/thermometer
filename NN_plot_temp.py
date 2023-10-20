from tensorflow import keras
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

# Load the saved model
loaded_model = keras.models.load_model('S5_humid')

data = pd.read_csv(
    'S5_test_edited.csv', usecols=[0, 2, 4, 6, 8])

# Extract features and target using the correct column names
X = data[['S1 Temp (C)', 'S2 Temp (C)', 'S3 Temp (C)',  'S4 Temp (C)']]
y = data['S5 Temp (C)']


# Split the data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Use the model to make predictions on the test data
y_pred = loaded_model.predict(X_test)

# Set colors for data points (red and orange)
colors = ['red' if pred < actual else 'orange' for pred,
          actual in zip(y_pred, y_test)]


# Create a scatter plot to compare actual and predicted values with different colors
plt.scatter(y_test, y_pred, alpha=0.5, c=colors)
plt.xlabel('Actual S5 Temperature (C)')
plt.ylabel('Predicted S5 Temperature (C)')
plt.title('Actual vs. Predicted S5 Temperature (C)')
# plt.xlim(28, 32.5)
# plt.ylim(28, 32.5)


# You can change the file format (e.g., .jpg, .pdf) and DPI as needed
# plt.savefig('S5_humid.png', dpi=1000)

# Display the plot (if you also want to show it)
plt.show()
