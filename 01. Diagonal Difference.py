n = int(input())
matrix = []
for _ in range(n):
    element = [int(el) for el in input().split(' ')]
    matrix.append(element)
first_diagonal = 0
second_diagonal = 0
col = n -1
for index in range(n):
    first_diagonal += matrix[index][index]
    second_diagonal += matrix[index][col]
    col -= 1
print(abs(second_diagonal - first_diagonal))
