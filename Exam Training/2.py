text = input()
matrix_size = int(input())
matrix = [[el for el in input()] for _ in range(matrix_size)]
number_of_commands = int(input())
player = "P"

def in_range(row_idx, col_idx):
    if 0 <= row_idx < len(matrix) and 0 <= col_idx < len(matrix):
        return True
    return False


def searching_player_position(row, col):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == player:
                row = r
                col = c
                return row, col


delta_directions = {'up': (-1, 0), 'down': (+1, 0),
                    'left': (0, -1), 'right': (0, +1)}

current_row = 0
current_col = 0
for _ in range(number_of_commands):
    direction = input()

    if direction in delta_directions:
        current_row, current_col = searching_player_position(current_row,current_col)
        next_row, next_col = current_row + delta_directions[direction][0], delta_directions[direction][1] + current_col
        if in_range(next_row, next_col):
            if matrix[next_row][next_col].isalpha():
                text += matrix[next_row][next_col]
            matrix[current_row][current_col] = "-"
            matrix[next_row][next_col] = player
        else:
            text = text[0:-1]


print(text)
for el in matrix:
    print("".join(el))
