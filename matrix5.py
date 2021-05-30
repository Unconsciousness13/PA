import sys

rows, cols = [int(el) for el in input().split(", ")]

matrix = []
position_top = None
position_bot = None
max_sum = -sys.maxsize
for row in range(rows):
    matrix.append([int(el) for el in input().split(",")])

for row in range(rows - 1, 0, -1):
    for col in range(cols - 1, 0, -1):
        current_sum = matrix[row][col] + matrix[row][col - 1] + matrix[row - 1][col] + matrix[row - 1][col - 1]
        if current_sum >= max_sum:
            max_sum = current_sum
            position_top = f"{matrix[row - 1][col - 1]} {matrix[row - 1][col]}"
            position_bot = f"{matrix[row][col - 1]} {matrix[row][col]}"

print(position_top)
print(position_bot)
print(max_sum)
