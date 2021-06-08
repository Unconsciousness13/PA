import math

n = int(input())
coins = 0
path = []
row = 0
col = 0
matrix = [[i for i in input().split(" ")] for el in range(n)]
for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == "P":
            row = r
            col = c
            break
current_row = row
current_col = col
while True:
    if coins >= 100:
        break
    command = input()

    if command == "left":
        if current_col > 0 and current_row in range(len(matrix)):
            if matrix[current_row][current_col - 1].isnumeric():
                coins += int(matrix[current_row][current_col - 1])
                path.append([current_row, current_col - 1])
                current_row, current_col = current_row, current_col - 1
                current_position = (current_row, current_col)
            else:
                if matrix[current_row][current_col - 1] == "X":
                    break
                else:
                    continue
        else:
            break

    elif command == "right":
        if current_col < n - 1 and current_row in range(len(matrix)):
            if matrix[current_row][current_col + 1].isnumeric():
                coins += int(matrix[current_row][current_col + 1])
                path.append([current_row, current_col + 1])
                current_row, current_col = current_row, current_col + 1
                current_position = (current_row, current_col)
            else:
                if matrix[current_row][current_col + 1] == "X":
                    break
                else:
                    continue
        else:
            break

    elif command == "up":
        if current_row > 0 and current_col in range(len(matrix)):
            if matrix[current_row - 1][current_col].isnumeric():
                coins += int(matrix[current_row - 1][current_col])
                path.append([current_row - 1, current_col])
                current_row, current_col = current_row - 1, current_col
                current_position = (current_row, current_col)
            else:
                if matrix[current_row - 1][current_col] == "X":
                    break
                else:
                    continue
        else:
            break
    elif command == "down":
        if current_row < n - 1 and current_col in range(len(matrix)):
            if matrix[current_row + 1][current_col].isnumeric():
                coins += int(matrix[current_row + 1][current_col])
                path.append([current_row + 1, current_col])
                current_row, current_col = current_row + 1, current_col
                current_position = (current_row, current_col)
            else:
                if matrix[current_row + 1][current_col] == "X":
                    break
                else:
                    continue
        else:
            break

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    coins = coins / 2
    coins = math.floor(coins)
    print(f"Game over! You've collected {coins} coins.")
print('Your path:')
print(*path, sep='\n')
