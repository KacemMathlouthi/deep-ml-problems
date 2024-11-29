import math

def sigmoid(z):
	return 1/(1+math.exp(-z))

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []
    for feature in features:
        zipped = zip(weights, feature)
        zipped = list(zipped)
        temp = 0
        for weight_per_feature in zipped:
              temp += weight_per_feature[0] * weight_per_feature[1]
        temp += bias
        temp = sigmoid(temp)
        probabilities.append(round(temp,4))
    mse = 0
    for i in range(len(probabilities)):
          mse += (probabilities[i] - labels[i])**2
    mse /= len(probabilities)
    return probabilities, mse
