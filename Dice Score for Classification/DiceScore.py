import numpy as np

def dice_score(y_true, y_pred):
    denom = np.sum(y_true) + np.sum(y_pred)
    if denom == 0:
        return 0.0
    res = 2 * np.sum(y_true & y_pred) / denom
    return round(res, 3)
