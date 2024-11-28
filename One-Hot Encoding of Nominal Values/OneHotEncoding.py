import numpy as np

def to_categorical(x, n_col=None):
    n_cols = np.max(x)
    result = []
    for i in range(len(x)):
        temp = [ j==x[i] for j in range(n_cols)]
        result.append(temp)
    return result
