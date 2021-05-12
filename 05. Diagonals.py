n = int(input())
fir = []
sec = []


def read_matrix(rows):
    matrix = []
    for _ in range(n):
        element = [int(el) for el in input().split(', ')]
        matrix.append(element)
    return matrix


def diagonals_sum(first_diagonal, second_diagonal):
    col = n - 1
    for index in range(n):
        first_diagonal += matrix[index][index]
        second_diagonal += matrix[index][col]
        fir.append(matrix[index][index])
        sec.append(matrix[index][col])
        col -= 1


matrix = read_matrix(n)
first_diagonal = 0
second_diagonal = 0

diagonals_sum(first_diagonal, second_diagonal)

print(f'First diagonal: {", ".join([str(x) for x in fir])}. Sum: {sum(fir)}')
print(f'Second diagonal: {", ".join([str(x) for x in sec])}. Sum: {sum(sec)}')
