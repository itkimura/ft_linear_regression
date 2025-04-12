
This project is a simple example of machine learning, where a Python program learns the relationship between car mileage and price using historical data.
By training on this data, the program finds the best-fit line that can be used to predict the price of a car based on its mileage.
One program performs the training and saves the model parameters, while the other uses those parameters to estimate prices for new mileage values.

## Machine Learning

**Machine learning** is a method that allows computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every task.
In this project, we use a basic form of machine learning called **supervised learning** — the model learns from example pairs of input (mileage) and output (price), and then uses what it learned to predict prices for new mileage values.


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