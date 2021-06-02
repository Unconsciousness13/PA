matrix_size = int(input())

matrix = [[int(el) for el in input().split()] for i in range(matrix_size)]

input_coordinates = input().split(" ")
coordinates = []
for el in input_coordinates:
    splited = el.split(",")
    one, two = splited[0], splited[1]
    one = int(one)
    two = int(two)
    coordinates.append([one, two])

for bomb in coordinates:
    row, col = bomb[0], bomb[1]
    row = int(row)
    col = int(col)
    for r in range(matrix_size):
        for c in range(matrix_size):
            if r == row and c == col:
                damage = (matrix[row][col])
                if 0 < r < matrix_size - 1 and 0 < col < matrix_size - 1:
                    if matrix[row - 1][col - 1] > 0:
                        matrix[row - 1][col - 1] -= damage
                    if matrix[row - 1][col + 1] > 0:
                        matrix[row - 1][col + 1] -= damage
                    if matrix[row - 1][col] > 0:
                        matrix[row - 1][col] -= damage
                    if matrix[row][col] > 0:
                        matrix[row][col - 1] -= damage
                    if matrix[row][col + 1] > 0:
                        matrix[row][col + 1] -= damage
                    if matrix[row + 1][col] > 0:
                        matrix[row + 1][col] -= damage
                    if matrix[row + 1][col + 1] > 0:
                        matrix[row + 1][col + 1] -= damage
                    if matrix[row + 1][col - 1] > 0:
                        matrix[row + 1][col - 1] -= damage
                    matrix[row][col] -= matrix[row][col]
                if 0 == r and 0 < col < matrix_size - 1:
                    if matrix[row][col - 1] > 0:
                        matrix[row][col - 1] -= damage
                    if matrix[row][col + 1] > 0:
                        matrix[row][col + 1] -= damage
                    if matrix[row + 1][col - 1] > 0:
                        matrix[row + 1][col - 1] -= damage
                    if matrix[row + 1][col] > 0:
                        matrix[row + 1][col] -= damage
                    if matrix[row + 1][col + 1] > 0:
                        matrix[row + 1][col + 1] -= damage
                    matrix[row][col] -= matrix[row][col]
                if 0 == r and c == 0:
                    if matrix[row + 1][col] > 0:
                        matrix[row + 1][col] -= damage
                    if matrix[row + 1][col + 1] > 0:
                        matrix[row + 1][col + 1] -= damage
                    if matrix[row][col + 1] > 0:
                        matrix[row][col + 1] -= damage
                    matrix[row][col] -= matrix[row][col]
                if 0 == r and c == matrix_size - 1:
                    if matrix[row + 1][col] > 0:
                        matrix[row + 1][col] -= damage
                    if matrix[row + 1][col - 1] > 0:
                        matrix[row + 1][col - 1] -= damage
                    if matrix[row][col - 1] > 0:
                        matrix[row][col - 1] -= damage
                    matrix[row][col] -= matrix[row][col]
                if r == matrix_size - 1 and c == 0:
                    if matrix[row - 1][col] > 0:
                        matrix[row - 1][col] -= damage
                    if matrix[row - 1][col + 1] > 0:
                        matrix[row - 1][col + 1] -= damage
                    if matrix[row][col + 1] > 0:
                        matrix[row][col + 1] -= damage
                    matrix[row][col] -= matrix[row][col]
                if r == matrix_size - 1 and c == matrix_size - 1:
                    if matrix[row - 1][col] > 0:
                        matrix[row - 1][col] -= damage
                    if matrix[row - 1][col - 1] > 0:
                        matrix[row - 1][col - 1] -= damage
                    if matrix[row][col - 1] > 0:
                        matrix[row][col - 1] -= damage
                    matrix[row][col] -= matrix[row][col]
                if col == 0 and 0 < row < matrix_size - 1:
                    if matrix[row][col + 1] > 0:
                        matrix[row][col + 1] -= damage
                    if matrix[row - 1][col] > 0:
                        matrix[row - 1][col] -= damage
                    if matrix[row - 1][col + 1] > 0:
                        matrix[row - 1][col + 1] -= damage
                    if matrix[row + 1][col + 1] > 0:
                        matrix[row + 1][col + 1] -= damage
                    if matrix[row + 1][col - 1] > 0:
                        matrix[row + 1][col] -= damage
                    matrix[row][col] -= matrix[row][col]
mat_sum = 0
alive_cells = 0
for el in matrix:
    for _ in el:
        if _ > 0:
            mat_sum += _
            alive_cells += 1
print(f"Alive cells: {alive_cells}")
print(f"Sum: {mat_sum}")
for el in matrix:
    print(*el)
