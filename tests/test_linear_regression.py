import unittest

from src.ft_linear_regression.linear_regression import hypothesis, predict_price, train_model
from src.ft_linear_regression.models import CarData


class TestLinearRegression(unittest.TestCase):

    def test_train_model_with_mock_data(self):
        # Mock data with km in 1000s
        mock_data = [
            CarData(km=0, price=20000),
            CarData(km=10, price=19500),
            CarData(km=20, price=19000),
            CarData(km=30, price=18500),
        ]

        theta0, theta1 = train_model(mock_data)
        self.assertEqual(theta0, 20250.0, delta=100)
        self.assertEqual(theta1, -66.67, delta=10)



    def test_hypothesis(self):
        # Test the hypothesis function with set parameters.
        self.assertEqual(18500.0, hypothesis(10000, 20000, -0.15))  # For a car with 10,000 km, the price should be $18,500.
        self.assertEqual(17000.0, hypothesis(20000, 20000, -0.15))  # For a car with 20,000 km, the price should be $17,000.



