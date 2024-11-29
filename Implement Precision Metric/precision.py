import numpy as np
def precision(y_true, y_pred):
    TP = np.sum(y_pred & y_true)
    FP = np.sum((y_pred == 1) & (y_true == 0))
    return TP/(TP+FP)