import numpy as np
def recall(y_true, y_pred):
    TP = np.sum(y_pred & y_true, axis= 0)
    print(TP)
    FN = np.sum(y_pred == 0 & y_true, axis= 0)
    print(FN)
    if TP + FN == 0:
        return 0
    recall = TP / (TP + FN)
    return round(recall, 3)