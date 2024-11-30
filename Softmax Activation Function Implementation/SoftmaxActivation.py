import math

def softmax(scores: list[float]) -> list[float]:
    denom = sum([math.exp(score) for score in scores])
    probabilities = [(math.exp(score) / denom) for score in scores]
    return round(probabilities, 4)