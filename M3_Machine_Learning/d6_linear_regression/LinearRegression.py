import numpy as np


class LinearRegression:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.b = 0
        self.a = 0

    def fit(self, x, y):
        #getting x and y
        self.x = x
        self.y = y

        # getting the means of x and y
        x_mean = np.mean(self.x)
        y_mean = np.mean(self.y)

        # initializing numerator and denominator for b (numerator is covariance for x and y, denominator is variance for x)
        b_num = 0
        b_den = 0

        # iterating over every element of X to get numerator and denominator
        for i in range(len(self.x)):
            b_num += (self.x[i] - x_mean) * (self.y[i] - y_mean)
            b_den += (self.x[i] - x_mean) ** 2

        # compute numerator and denominator to get b
        self.b = b_num / b_den

        # getting a
        self.a = y_mean - (self.b * x_mean)
        
        return self

    def predict(self, x):
        # predicting y points
        y_pred = self.a + (self.b * x)
        return y_pred
