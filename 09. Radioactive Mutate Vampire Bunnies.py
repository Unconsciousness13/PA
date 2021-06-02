def find_start_position(field):
    for row_i in range(len(field)):
        for col_i in range(len(field[row_i])):
            if field[row_i][col_i] == "P":
                return row_i, col_i


def moving(row_i, col_i, direction):
    if direction == "U":
        row_i -= 1
    elif direction == "R":
        col_i += 1
    elif direction == "D":
        row_i += 1
    elif direction == "L":
        col_i -= 1
    return row_i, col_i


def locate_bunnies(field, rows_n, cols_n):
    sectors = set()
    for row_i in range(rows_n):
        for col_i in range(cols_n):
            if field[row_i][col_i] == "B":
                if 0 <= row_i - 1 < rows_n:
                    sectors.add((row_i - 1, col_i))
                if 0 <= col_i + 1 < cols_n:
                    sectors.add((row_i, col_i + 1))
                if 0 <= row_i + 1 < rows_n:
                    sectors.add((row_i + 1, col_i))
                if 0 <= col_i - 1 < cols_n:
                    sectors.add((row_i, col_i - 1))
    return sectors


def bunnies_spawning(field, bunnies_locations, game_lost):
    for sector in bunnies_locations:
        row_i, col_i = sector
        if field[row_i][col_i] == "P":
            game_lost = True
        field[row_i][col_i] = "B"
    return field, game_lost


(rows, cols) = map(int, input().split())

lair = []
for _ in range(rows):
    lair.append(list(input()))

directions = list(input())

row_idx, col_idx = find_start_position(lair)

player_escaped = False
player_died = False

for move in directions:
    if player_escaped or player_died:
        break
    lair[row_idx][col_idx] = "."
    (next_row_idx, next_col_idx) = moving(row_idx, col_idx, move)
    if 0 <= next_row_idx < rows and 0 <= next_col_idx < cols:
        row_idx, col_idx = (next_row_idx, next_col_idx)
        if lair[row_idx][col_idx] == "B":
            player_died = True
        else:
            lair[row_idx][col_idx] = "P"
    else:
        player_escaped = True
    bunnies_sectors = locate_bunnies(lair, rows, cols)
    lair, player_died = bunnies_spawning(lair, bunnies_sectors, player_died)

[print(*line, sep="") for line in lair]

if player_escaped:
    print(f"won: {row_idx} {col_idx}")
elif player_died:
    print(f"dead: {row_idx} {col_idx}")