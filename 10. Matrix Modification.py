matrix_size = int(input())
matrix = []
for _ in range(matrix_size):
    mat_row = [int(x) for x in input().split()]
    matrix.append(mat_row)
command = input()
while not command == "END":
    action, row, col, value = command.split(" ")
    row = int(row)
    col = int(col)
    value = int(value)
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        if action == "Add":
            for r in range(matrix_size):
                for c in range(len(matrix)):
                    if r == row and c == col:
                        matrix[r][c] += value

        if action == "Subtract":
            for r in range(matrix_size):
                for c in range(len(matrix)):
                    if r == row and c == col:
                        matrix[r][c] -= value

    else:
        print("Invalid coordinates")
    command = input()
[print(" ".join([str(x) for x in r])) for r in matrix]
