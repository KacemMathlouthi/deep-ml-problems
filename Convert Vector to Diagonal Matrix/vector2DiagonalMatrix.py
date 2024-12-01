import numpy as np

def make_diagonal(x):
    n = len(x)
    diagonal = np.zeros((n, n))
    for i in range(n):
        diagonal[i, i] = x[i]
    return diagonal