rows = int(input())
matrix = []
even = []
for _ in range(rows):
    row_nums = [int(num) for num in input().split(', ')]
    matrix.append(row_nums)
for i in matrix:
    _ = [int(el) for el in i if el % 2 == 0]
    even.append(_)
print(even)