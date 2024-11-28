import numpy as np

def to_categorical(x, n_col=None):
    n_cols = np.max(x) + 1
    result = [[1 if j == x[i] else 0 for j in range(n_cols)] for i in range(len(x))]
    return result
