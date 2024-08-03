import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load data from CSV
data = pd.read_csv('Responses.csv')

# Ensure the data contains only numeric responses for the questions
# Assuming the MBTI type is in the last column and the rest are numeric responses
X = data.iloc[:, :-1].apply(pd.to_numeric, errors='coerce').fillna(0).values
y = data.iloc[:, -1].values

# Encode the MBTI types as numerical labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Standardize the input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(len(label_encoder.classes_), activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, validation_data=(X_val, y_val))

# Function to determine MBTI type
def determine_mbti(answers, model, scaler, label_encoder):
    # Ensure the input data has the correct shape
    input_data = np.array(answers).reshape(1, -1)
    
    # Check if the number of features in input_data matches the model's input shape
    if input_data.shape[1] != scaler.mean_.shape[0]:
        raise ValueError(f"Input data has {input_data.shape[1]} features, but the scaler was fitted on {scaler.mean_.shape[0]} features.")
    
    # Scale the input data
    input_data_scaled = scaler.transform(input_data)
    
    # Predict MBTI type using the model
    predicted_mbti_index = np.argmax(model.predict(input_data_scaled), axis=-1)
    predicted_mbti = label_encoder.inverse_transform(predicted_mbti_index)
    
    return predicted_mbti[0]

# Read the responses from the CSV file and determine MBTI types
responses = data.iloc[:, :-1].apply(pd.to_numeric, errors='coerce').fillna(0).values
predicted_mbti_types = []

for response in responses:
    mbti_type = determine_mbti(response, model, scaler, label_encoder)
    predicted_mbti_types.append(mbti_type)

# Add the predicted MBTI types to the original data
data['Predicted MBTI'] = predicted_mbti_types

# Save the results to a new CSV file
data.to_csv('Responses_with_Predicted_MBTI.csv', index=False)

print("MBTI personality types have been predicted and saved to 'Responses_with_Predicted_MBTI.csv'.")