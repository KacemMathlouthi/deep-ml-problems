import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        return None
    cofactor_matrix = [
        [matrix[1][1], -matrix[0][1]],
        [-matrix[1][0], matrix[0][0]]
    ]
    inverse = (1/det) * np.array(cofactor_matrix)
    return inverse