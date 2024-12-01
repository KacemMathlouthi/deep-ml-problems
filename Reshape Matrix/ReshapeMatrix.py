import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    rows, cols = new_shape
    reshaped_matrix = []
    k = 0
    temp = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            k += 1
            temp.append(a[i][j])
            if k == cols:
                reshaped_matrix.append(temp)
                temp = []
                k = 0
    return reshaped_matrix