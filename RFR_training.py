import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load your data
data = pd.read_csv('S5_edited.csv', usecols=[1, 3, 5, 7, 9])

# Extract features and target
X = data[['S1 Humidity (%)', 'S2 Humidity (%)',
          'S3 Humidity (%)', 'S4 Humidity (%)']]
y = data['S5 Humidity (%)']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Create a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model on the test set
test_score = model.score(X_test, y_test)
print(f"Test Score (R-squared): {test_score:.2f}")

joblib.dump(model, 'S5_humid_RFR_model.pkl')
