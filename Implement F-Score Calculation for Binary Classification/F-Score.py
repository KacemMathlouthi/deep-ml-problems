import numpy as np

def f_score(y_true, y_pred, beta):
    tp = np.sum(y_pred & y_true)
    fp = np.sum((y_pred==1) & (y_true==0))
    fn = np.sum((y_pred==0) & (y_true==1))

    recall = tp / (tp + fn)
    precision = tp / (tp + fp)

    Fbeta = (precision * recall * (1 + beta**2)) / ((beta**2) * precision + recall)
    
    return round(Fbeta, 3)