from typing import List

from src.ft_linear_regression.models import CarData


# The hypothesis function for linear regression, which predicts the price of a car given its mileage.
# It's a simple linear function: y = theta0 + theta1 * x
def hypothesis(mileage: int, theta0: float, theta1: float) -> float:
    return theta0 + theta1 * mileage


def train_model(data: List[CarData], learning_rate: float, num_iterations: int):
    theta0, theta1 = 0.0, 0.0
    # Calculate the size of the data
    m = len(data)

    # Perform gradient descent for the given number of iterations
    for _ in range(num_iterations):
        tmp_theta0, tmp_theta1 = 0.0, 0.0

        # Calculate the sum of the differences between the predicted and actual prices
        for car_data in data:
            # Predict the price using the current theta0 and theta1
            prediction = hypothesis(car_data.km, theta0, theta1)
            # Accumulate the difference between the prediction and the actual price
            tmp_theta0 += (prediction - car_data.price)
            tmp_theta1 += (prediction - car_data.price) * car_data.km

        # Calculate the average difference and scale it by the learning rate
        tmp_theta0 *= learning_rate / m
        tmp_theta1 *= learning_rate / m

        # Update theta0 and theta1 simultaneously
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

    # Return the final theta0 and theta1 after training
    return theta0, theta1


def predict_price(mileage, data_list):
    # Assume theta0 and theta1 are obtained from training
    theta0 = 0
    theta1 = 0
    # Calculate predicted price using the hypothesis
    return hypothesis(mileage, theta0, theta1)