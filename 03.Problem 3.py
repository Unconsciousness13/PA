def get_magic_triangle(n):
    matrix = []
    number = 1
    for num in range(1, n + 1):
        matrix.append([number] * num)
    for r in range(0, n):
        for c in range(len(matrix[r])):
            if r - 1 > 0 and c - 1 >= 0:
                if c in range(r):
                    matrix[r][c] = matrix[r - 1][c - 1] + matrix[r - 1][c]
            else:
                matrix[r][c] = matrix[0][0]

    return matrix


get_magic_triangle(5)
