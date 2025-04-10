import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dummy data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Model training
model = LinearRegression()
model.fit(X, y)

# Prediction
x_test = np.array([[6]])
print("Prediction for 6:", model.predict(x_test))

# Plotting
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title("Linear Regression Fit")
plt.show()
