text = input()
n = int(input())
matrix = [[el for el in input()] for rows in range(n)]
m = int(input())
row = 0
col = 0


for itt in range(m):
    command = input()
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "P":
                row = r
                col = c
                break
    current_row = row
    current_col = col
    if command == "up":
        if current_row > 0 and current_col in range(len(matrix)):
            if matrix[current_row - 1][current_col].isalpha():
                text += matrix[current_row - 1][current_col]
                matrix[current_row][current_col] = "-"
                matrix[current_row - 1][current_col] = "P"
            else:
                matrix[current_row][current_col] = "-"
                matrix[current_row - 1][current_col] = "P"
        else:
            text = text[0:-1]

    elif command == "down":
        if current_row < n - 1 and current_col in range(len(matrix)):
            if matrix[current_row + 1][current_col].isalpha():
                text += matrix[current_row + 1][current_col]
                matrix[current_row][current_col] = "-"
                matrix[current_row + 1][current_col] = "P"
            else:
                matrix[current_row][current_col] = "-"
                matrix[current_row + 1][current_col] = "P"
        else:
            text = text[0:-1]

    elif command == "right":
        if current_col < n - 1 and current_row in range(len(matrix)):
            if matrix[current_row][current_col + 1].isalpha():
                text += matrix[current_row][current_col + 1]
                matrix[current_row][current_col] = "-"
                matrix[current_row][current_col + 1] = "P"
            else:
                matrix[current_row][current_col] = "-"
                matrix[current_row][current_col + 1] = "P"
        else:
            text = text[0:-1]
    elif command == "left":
        if current_col > 0 and current_row in range(len(matrix)):
            if matrix[current_row][current_col - 1].isalpha():
                text += matrix[current_row][current_col - 1]
                matrix[current_row][current_col] = "-"
                matrix[current_row][current_col - 1] = "P"
            else:
                matrix[current_row][current_col] = "-"
                matrix[current_row][current_col - 1] = "P"
        else:
            text = text[0:-1]
print(text)
for el in matrix:
    print("".join(el))
