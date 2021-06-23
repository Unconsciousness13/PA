chess_table = [[el for el in input().split()] for c in range(8)]
n = 8
KING = "K"
QUEEN = "Q"
queens = []


def in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


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

for row in range(n):
    for col in range(n):
        if chess_table[row][col] == KING:
            for delta in deltas:
                current_row = delta[0] + row
                current_col = delta[1] + col
                while in_range(current_row, current_col, n):
                    if chess_table[current_row][current_col] == QUEEN:
                        queens.append([current_row, current_col])
                        break
                    current_row += delta[0]
                    current_col += delta[1]

if queens:
    for queen in queens:
        print(queen)
else:
    print("The king is safe!")
