def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	b = [[row[i] for row in a] for i in range(len(a[0]))]
	return b
