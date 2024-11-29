import numpy as np
def recall(y_true, y_pred):
    TP = np.sum(y_pred & y_true, axis= 0)
    FN = np.sum((y_pred == 0) & (y_true == 1), axis= 0)
    if TP + FN == 0:
        return 0
    recall = TP / (TP + FN)
    return round(recall, 3)