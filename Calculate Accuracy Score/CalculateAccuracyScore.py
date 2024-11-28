import numpy as np

def accuracy_score(y_pred, y_true):
    correct = 0
    for i in range(y_pred.shape[0]):
        if y_pred[i] == y_true[i]:
            correct += 1
    return correct/y_pred.shape[0]