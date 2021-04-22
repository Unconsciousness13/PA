import itertools

rows, cols = [int(element) for element in input().split(', ')]
matrix = [[int(number) for number in input().split(', ')] for _ in range(rows)]
total = sum(itertools.chain(*matrix))
print(total)
print(matrix)
