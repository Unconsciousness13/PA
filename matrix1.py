import itertools
rows,cols = [int(el) for el in input().split(", ")]
matrix = [[int(number) for number in input().split(", ")] for _ in range(rows)]
result = sum(itertools.chain(*matrix))
print(result)
print(matrix)