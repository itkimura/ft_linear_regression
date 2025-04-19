
This project is a simple example of machine learning, where a Python program learns the relationship between car mileage and price using historical data.
By training on this data, the program finds the best-fit line that can be used to predict the price of a car based on its mileage.
One program performs the training and saves the model parameters, while the other uses those parameters to estimate prices for new mileage values.

## Machine Learning

**Machine learning** is a method that allows computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every task.
In this project, we use a basic form of machine learning called **supervised learning** — the model learns from example pairs of input (mileage) and output (price), and then uses what it learned to predict prices for new mileage values.

### Gradient Descent

Gradient Descent is an optimization algorithm used to minimize the cost function in a manageable amount of time. It is an iterative algorithm that takes steps proportional to the negative of the gradient (or approximate gradient) of the function at the current point.
In the context of this project, gradient descent is used to find the optimal values of `θ0` and `θ1` that minimize the cost function (Mean Squared Error) and give the best model for predicting car prices based on mileage.

Here's a high-level overview of how gradient descent works:

1. Initialize `θ0` and `θ1` with some values, commonly 0 or a small random value.
2. Calculate the cost (the error of the prediction) with the initial `θ0` and `θ1`.
3. Use partial derivatives of the cost function to adjust the `θ0` and `θ1` values in the direction that decreases the cost.
4. Repeat the above steps until the cost stops decreasing significantly or a maximum number of iterations is reached.

The learning rate is a critical parameter in gradient descent. It determines the size of the steps we take to reach the minimum. If the learning rate is too high, we may step over the minimum and oscillate around it. If it is too low, the algorithm may take too long to converge.
Gradient Descent allows us to find a good fit for our data, improving the accuracy of our predictions while keeping computation time reasonable.

## Linear Regression

Linear regression is a type of predictive statistical analysis used to estimate the value of a **dependent variable** (output) based on one or more **independent variables** (inputs).

In this project, we apply **simple linear regression** to predict the **price of a car** based on its **mileage**.

---

### Simple Linear Regression

In its simplest form, linear regression assumes a linear (straight-line) relationship between the input and output variables. The model is represented by the equation:

```ini
price = θ1 × mileage + θ0
```
Where:
- `price` is the **dependent variable** (the value we want to predict).
- `mileage` is the **independent variable** (the input used to make predictions).
- `θ1` (theta1) is the slope of the line (also known as the regression coefficient), representing how much the price changes as mileage increases.
- `θ0` (theta0) is the y-intercept, indicating the estimated price when mileage is 0.

### Car Price vs. Mileage
The following plot shows the actual data points (in blue) and the best-fit regression line (in red) for our dataset:
![Car Price vs Mileage](images/linear_regression_car_price.png)


### Objective
The goal of linear regression is to find the best values for the parameters θ0 and θ1 that minimize the error between predicted and actual prices.

This error is typically measured using a cost function such as Mean Squared Error (MSE), which calculates the average squared difference between the predicted and actual values.