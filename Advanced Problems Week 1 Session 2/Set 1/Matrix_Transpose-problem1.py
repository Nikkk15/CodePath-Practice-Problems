def transpose(matrix):
    new_matrix = [[], [], []]
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            new_matrix[k].append(matrix[i][k])
    return new_matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))