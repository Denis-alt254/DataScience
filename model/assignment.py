import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

# 1. Load and Prepare the Dataset

# Load dataset
file_path = 'boston-housing-dataset.csv'
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Dataset not found at: {file_path}")

df = pd.read_csv(file_path)

# Drop index column if present
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Define features and target
X = df.drop('MEDV', axis=1)
y = df['MEDV']

# 2. Train the Linear Regression Model

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model performance
score = model.score(X_test, y_test)
print(f"✅ Model trained successfully.\nR² score on test data: {score:.2f}")

# Save the trained model
model_filename = 'boston_price_model.pkl'
joblib.dump(model, model_filename)
print(f"📦 Model saved as '{model_filename}'")

# 3. Predict Using Hypothetical Input

# Create a sample input dictionary 
sample_input = pd.DataFrame([{
    'CRIM': 0.05,
    'ZN': 20.0,
    'INDUS': 5.0,
    'CHAS': 0,
    'NOX': 0.45,
    'RM': 6.5,
    'AGE': 60.0,
    'DIS': 4.0,
    'RAD': 4,
    'TAX': 300.0,
    'PTRATIO': 18.0,
    'B': 390.0,
    'LSTAT': 10.0
}])

# Ensure all columns match training data
for col in X.columns:
    if col not in sample_input.columns:
        sample_input[col] = 0
sample_input = sample_input[X.columns]

# Load the saved model
loaded_model = joblib.load(model_filename)

# Make prediction
predicted_price = loaded_model.predict(sample_input)
print(f"💰 Predicted House Price: ${predicted_price[0]*1000:.2f}")