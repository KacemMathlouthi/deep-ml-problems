def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        means = [sum(row)/len(row) for row in matrix]
    else:
        matrix_transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        means = [sum(row)/len(row) for row in matrix_transposed]
    return means