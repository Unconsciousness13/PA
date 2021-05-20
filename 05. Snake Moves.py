from collections import deque

row_count, col_count = [int(x) for x in input().split()]
text = deque(input())

matrix = []
for _ in range(row_count):
    matrix.append(['' for _ in range(col_count)])

for row in range(row_count):
    if row % 2 == 0:
        for col in range(col_count):
            element = text.popleft()
            matrix[row][col] = element
            text.append(element)

    else:
        for col in range(col_count - 1, -1, -1):
            element = text.popleft()
            matrix[row][col] = element
            text.append(element)
for el in matrix:
    print(''.join(el))
