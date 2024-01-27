import numpy as np

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

def max_determinant_multiply():
    n, m = map(int, input().split())

    matrices = []

    for _ in range(n):
        matrix = np.array([list(map(int, input().split())) for _ in range(m)])
        matrices.append(matrix)

    max_det = -1
    max_det_matrices = None

    for i in range(n):
        for j in range(i + 1, n):
            product_matrix = np.dot(matrices[i], matrices[j])
            determinant = calculate_determinant(product_matrix)

            if determinant > max_det:
                max_det = determinant
                max_det_matrices = (i, j)
    print(max_det_matrices)

    if calculate_determinant(matrices[max_det_matrices[0]]) > calculate_determinant(matrices[max_det_matrices[1]]):
        result_matrix = np.dot(matrices[max_det_matrices[0]], matrices[max_det_matrices[1]])
    else:
        result_matrix = np.dot(matrices[max_det_matrices[1]], matrices[max_det_matrices[0]])


    inverted_result = np.linalg.inv(result_matrix)

    for row in inverted_result:
        print(" ".join(f"{value:.3f}" for value in row))

max_determinant_multiply()
