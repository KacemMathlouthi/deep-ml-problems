import numpy as np

def jaccard_index(y_true, y_pred):
    if len(y_pred) == 0 or len(y_true) == 0:
        return 0 
    intersect = np.sum(y_true & y_pred) 
    union = np.sum(y_pred, axis = 0) + np.sum(y_true, axis = 0) - intersect
    if union == 0:
        return 0
    result = intersect / union
    return round(result, 3)