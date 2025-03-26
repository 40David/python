import numpy as np
from sklearn.linear_model import LinearRegression

# Given data
population = np.array([5, 7, 15, 22, 27, 36]).reshape(-1, 1)
sales = np.array([28, 40, 65, 80, 96, 130])


model = LinearRegression()
model.fit(population, sales)

# Predict sales for a population of 45 million
predicted_sales = model.predict(np.array([[45]]))

print(f"Estimated washing machines sold in 2026: {predicted_sales[0]:.2f} ('000)")
