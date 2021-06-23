board = [[el for el in input().split()] for i in range(8)]
KING = "K"
QUEEN = "Q"


def found_the_king(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == KING:
                return (row, col)


def in_range(value, max_value):
    return 0 <= value < max_value


def searching_with_deltas(board, king, deltas):
    row_count = len(board)
    col_count = len(board[0])
    delta_row, delta_col = deltas
    row_index, col_index = king
    while True:
        if not in_range(row_index, row_count) or not in_range(col_index, col_count):
            return None
        if board[row_index][col_index] == QUEEN:
            return [row_index, col_index]

        row_index += delta_row
        col_index += delta_col


def capturing_queens(board, king):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1)
    ]
    queens = [searching_with_deltas(board, king, delta) for delta in deltas]

    return [queen for queen in queens if queen]


def print_result(queens):
    if queens:
        for queen in queens:
            print(queen)
    else:
        print("The king is safe!")


king = found_the_king(board)
queens = capturing_queens(board, king)
print_result(queens)

