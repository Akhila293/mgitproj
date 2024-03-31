import pandas as pd
import warnings

# Suppress specific warning
warnings.filterwarnings("ignore", message="X does not have valid feature names*", module="sklearn")

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

def calc(annual_rainfall, fertilizer, pesticide, production):
    input_data = scaler.transform([[annual_rainfall, fertilizer, pesticide, production]])
    predicted_yield = model.predict(input_data)
    return predicted_yield[0]

# Load the dataset
#dataset = pd.read_csv('data\crop_yield.csv')
dataset = pd.read_csv(r"C:\Users\HP\Downloads\crop_yield.csv")

# Drop rows with missing values
dataset.dropna(inplace=True)

# Separate features and target variable
X = dataset[['Annual_Rainfall', 'Fertilizer', 'Pesticide', 'Production']]
y = dataset['Yield']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the Random Forest model
model = RandomForestRegressor(random_state=42)
model.fit(X_train_scaled, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test_scaled)

# Calculate mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)