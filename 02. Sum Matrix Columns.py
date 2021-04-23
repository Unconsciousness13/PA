rows, cols = [int(n) for n in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(n) for n in input().split(' ')])

for j in range(cols):
    total = 0
    for row in matrix:
        total += row[j]
    print(total)
