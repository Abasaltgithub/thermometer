import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load your data
data = pd.read_csv(
    'sensor_data_no_duplicates_1.csv', usecols=[1, 3, 5, 7, 9])

# Extract features and target
X = data[['S1 Humidity (%)', 'S2 Humidity (%)',
          'S3 Humidity (%)', 'S4 Humidity (%)']]
y = data['S5 Humidity (%)']

# X = data[['S1 Temp (C)', 'S2 Temp (C)', 'S3 Temp (C)', 'S4 Temp (C)']]
# y = data['S5 Temp (C)']

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

# Build a neural network model
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(4,)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    # Use linear activation for regression
    keras.layers.Dense(1, activation='linear')
])

# Experiment with different optimizers (e.g., Adam, RMSprop)
optimizer = keras.optimizers.Adam(learning_rate=0.001)

model.compile(optimizer=optimizer, loss='mean_squared_error')

# Implement a learning rate scheduler
lr_scheduler = keras.callbacks.LearningRateScheduler(
    lambda epoch: 1e-6 * 10**(epoch / 20))

# Implement early stopping
early_stopping = keras.callbacks.EarlyStopping(
    patience=20, restore_best_weights=True)

# Train the model
history = model.fit(X_train, y_train, epochs=200, batch_size=16, validation_data=(X_val, y_val),
                    callbacks=[lr_scheduler, early_stopping])

# Evaluate the model on the test set
test_loss = model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss}")

# Save the trained model to a file
model.save('humid_model_1.h5')
