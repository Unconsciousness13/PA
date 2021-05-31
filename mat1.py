def read_matrix(rows):
    matrix = []

    for _ in range(rows):
        matrix.append([])
        for el in input().split():
            inner_list = matrix[-1]
            inner_list.append(int(el))

    return matrix


n = int(input())
matrix = read_matrix(n)
left_diagonal = 0
right_diagonal = 0

for i in range(n):
    left_diagonal += matrix[i][i]

for i in range(n):
    right_diagonal += matrix[len(matrix) - 1 - i][i]

print(abs(right_diagonal - left_diagonal))
