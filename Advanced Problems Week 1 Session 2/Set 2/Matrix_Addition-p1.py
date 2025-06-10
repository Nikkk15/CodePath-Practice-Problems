# Problem 1: Matrix Addition
# Write a function add_matrices() that accepts to n x m matrices matrix1 and matrix2.
# The function should return an n x m matrix sum_matrix that is the sum of the given
# matrices such that each value in sum_matrix is the sum of values of corresponding elements in matrix1 and matrix2.

def add_matrices(matrix1, matrix2):
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix2[i][j] += matrix1[i][j]
    return matrix2

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(add_matrices(matrix1, matrix2))
# Example Output:

# [
#     [10, 10, 10],
#     [10, 10, 10],
#     [10, 10, 10]
# ]