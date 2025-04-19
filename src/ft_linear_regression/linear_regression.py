from typing import List

from src.ft_linear_regression.models import CarData


# The hypothesis function for linear regression, which predicts the price of a car given its mileage.
# It's a simple linear function: y = theta0 + theta1 * x
def hypothesis(km: int, theta0: float, theta1: float) -> float:
    return theta0 + (theta1 * km)


# This function calculates the cost function for the current values of theta0 and theta1.
# It uses the Mean Squared Error cost function: 1/2m * Σ(y - (theta1*x + theta0))^2
def calculate_cost_function(m, theta0, theta1, data):
    total_cost = 0
    for i in range(m):
        x = data[i].km
        y = data[i].price
        total_cost += (y - (theta1 * x + theta0)) ** 2
    return total_cost / (2 * m)


# This function updates the values of theta0 and theta1 based on the partial derivatives of the cost function.
# It uses the formula for gradient descent: theta = theta - learning_rate * derivative
def update_weights(m, theta0, theta1, data, learning_rate):
    theta0_deriv = 0
    theta1_deriv = 0
    for i in range(m):
        x = data[i].km
        y = data[i].price
        theta0_deriv += - (2 / m) * (y - (theta1 * x + theta0))  # derivative with respect to theta0
        theta1_deriv += - (2 / m) * x * (y - (theta1 * x + theta0))  # derivative with respect to theta1
    theta0 -= (theta0_deriv * learning_rate)  # update theta0
    theta1 -= (theta1_deriv * learning_rate)  # update theta1
    return theta0, theta1


# This function performs the gradient descent optimization technique.
# It initializes theta0 and theta1 and performs a specified number of gradient descent steps.
# At each step, it calculates the cost function and updates theta0 and theta1.
def gradient_descent(data: List[CarData], starting_theta0=0, starting_theta1=0, learning_rate=0.0001, num_iterations=1000):
    theta0 = starting_theta0
    theta1 = starting_theta1
    m = len(data)
    for _ in range(num_iterations):
        theta0, theta1 = update_weights(m, theta0, theta1, data, learning_rate)
    return theta0, theta1


def predict_price(mileage, theta0, theta1):
    # Calculate predicted price using the hypothesis
    return hypothesis(mileage, theta0, theta1)


def train_and_predict(data: List[CarData], mileage: int, starting_theta0=0, starting_theta1=0, learning_rate=0.0001,
                      num_iterations=1000):
    # First, train the model using gradient descent to get theta0 and theta1
    theta0, theta1 = gradient_descent(data, starting_theta0, starting_theta1, learning_rate, num_iterations)

    # Then, use the trained model to predict the price for the given mileage
    predicted_price = hypothesis(mileage, theta0, theta1)

    return predicted_price
