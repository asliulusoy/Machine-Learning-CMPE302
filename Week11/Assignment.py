# Import necessary libraries including scikit-learn
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

'''
Design and implement a Python program to predict the price of a house based
on its features using Random Forest Regression. Your program should take
input for various features such as area, number of rooms, and location, and
predict the price of the house.

'''

#  Generate or use a suitable dataset containing house features and prices.
data = {
    'area': [1000, 2000, 1500, 3000, 3500, 4000],
    'rooms': [2, 3, 3, 4, 4, 5],
    'location': [1, 2, 3, 2, 1, 3], 
    'price': [300000, 500000, 400000, 650000, 600000, 800000]
}

df = pd.DataFrame(data)

X = df[['area', 'rooms', 'location']]
y = df['price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Regression model using the training data.
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#  Use the trained model to make predictions on the test set.
y_pred = model.predict(X_test)

# Evaluate the prediction performance using metrics such as mean squared error.
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Implement proper error handling and input validation.
def predict_price(area, rooms, location):
    try:
        if not isinstance(area, (int, float)) or area <= 0:
            raise ValueError("area value should be greater than 0")
        if not isinstance(rooms, int) or rooms <= 0:
            raise ValueError("number value should e greater than 0")
        if not isinstance(location, int) or location not in [1, 2, 3]:
            raise ValueError("location is not defined.")
        new_house = pd.DataFrame([[area, rooms, location]], columns=['area', 'rooms', 'location'])
        
        predicted_price = model.predict(new_house)
        return predicted_price[0]
    except Exception as e:
        return str(e)
# Test
print(f"Predicted Value: {predict_price(2000, 3, 1)}")