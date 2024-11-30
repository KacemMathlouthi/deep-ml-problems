import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    max = np.max(scores)
    sum = np.sum(np.exp(scores - max))
    log_sm = scores - max - np.log(sum)
    return log_sm