rows, cols = [int(num) for num in input().split()]
max_sum = -999999
matrix = []
max_matrix_3x3 = []
for _ in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)
for row in range(rows - 2):
    for col in range(cols - 2):
        sub_matrix = []
        current_sum = 0
        row_counter = 0
        for r in range(row, row + 3):
            sub_matrix.append([])
            for c in range(col, col + 3):
                sub_matrix[row_counter].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_counter += 1
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix_3x3 = sub_matrix
print(f"Sum = {max_sum}")

for row in max_matrix_3x3:
    print(" ".join([str(x) for x in row]))
