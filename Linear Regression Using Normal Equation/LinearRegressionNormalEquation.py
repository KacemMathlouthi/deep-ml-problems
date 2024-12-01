import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y)
    X_transposed = X.T
    theta = np.linalg.inv(X_transposed.dot(X)).dot(X_transposed).dot(y)
    theta = np.round(theta, 4)
    return theta