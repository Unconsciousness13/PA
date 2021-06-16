board_size = int(input())
bombs_number = int(input())
BOMBA = "*"
EMPTY = 0
board = [[int(el) for el in "0" * board_size] for ele in range(board_size)]


def bombs_positions():
    bomb_coordinates = []
    for position in range(bombs_number):
        data = [int(el) for el in input()[1:][:-1].split(", ")]
        bomb_coordinates.append(data)
    return bomb_coordinates


bomb_list = bombs_positions()


def making_the_table_with_bombs(board):
    for bomb in bomb_list:
        bomb_row, bomb_col = bomb[0], bomb[1]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == bomb_row and c == bomb_col:
                    board[r][c] = BOMBA
    return board


board_with_bombs = making_the_table_with_bombs(board)
deltas = [(0, -1), (-1, -1), (-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1), ]
number = 0
for row in range(len(board_with_bombs)):
    for column in range(len(board_with_bombs[0])):
        current_row = row
        current_col = column
        current_index = board_with_bombs[current_row][current_col]
        if not current_index == BOMBA:
            for delt in deltas:
                delta_row, delta_col = delt[0], delt[1]
                delta_row_index, delta_col_index = delta_row + current_row, delta_col + current_col
                if 0 <= delta_row_index < len(board_with_bombs) and 0 <= delta_col_index < len(board_with_bombs):
                    for el in bomb_list:
                        bob_row = el[0]
                        bob_col = el[1]
                        if delta_row_index == bob_row and delta_col_index == bob_col:
                            number += 1
                            break
            board_with_bombs[current_row][current_col] = number
            number = 0
final_board = []
for i in range(len(board_with_bombs)):
    result = ''
    for el in range(len(board_with_bombs[i])):
        result += str(board_with_bombs[i][el])
        if el < len(board_with_bombs) - 1:
            result += " "
    final_board.append(result)

for el in final_board:
    print(el)
