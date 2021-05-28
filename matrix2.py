rows, cols = [int(el) for el in input().split(", ")]
matrix = [[int(number) for number in input().split(" ")] for _ in range(rows)]

for index in range(cols):
    result = 0
    for row in matrix:
        result += row[index]
    print(result)
