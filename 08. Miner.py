field_size = int(input())
directions = list(input().split(" "))
field = [[el for el in input().split()] for r in range(field_size)]

regular_position_field = "*"
end_of_route = "e"
coal = "c"
miner_start = "s"


def miner_position(row, col):
    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col] == miner_start:
                return row, col

    return row, col


def valid_index(row, col):
    if 0 <= row < len(field) and 0 <= col < len(field):
        return True
    else:
        pass


counter = 0
coal_counter = 0
cur_row = 0
cur_col = 0
current_position = miner_position(cur_row, cur_col)
cur_row = current_position[0]
cur_col = current_position[1]
for r in range(field_size):
    for c in range(field_size):
        if field[r][c] == "c":
            coal_counter += 1
while not counter == len(directions):

    for direction in directions:
        if counter == len(directions):
            break
        counter += 1
        if direction == "left":
            if valid_index(cur_row, cur_col - 1):
                if field[cur_row][cur_col - 1] == "c":
                    coal_counter -= 1
                    if coal_counter == 0:
                        field[cur_row][cur_col] = "*"
                        cur_col -= 1
                        break
                if field[cur_row][cur_col - 1] == "e":
                    field[cur_row][cur_col - 1] = "s"
                    print(f"Game over! ({cur_row}, {cur_col - 1})")
                    exit()
                field[cur_row][cur_col - 1] = "s"
                field[cur_row][cur_col] = "*"
                cur_col -= 1
            else:
                continue
        elif direction == "up":
            if valid_index(cur_row - 1, cur_col):
                if field[cur_row - 1][cur_col] == "c":
                    coal_counter -= 1
                    if coal_counter == 0:
                        field[cur_row][cur_col] = "*"
                        cur_row -= 1
                        break
                if field[cur_row - 1][cur_col] == "e":
                    field[cur_row - 1][cur_col] = "s"
                    print(f"Game over! ({cur_row - 1}, {cur_col})")
                    exit()
                field[cur_row - 1][cur_col] = "s"
                field[cur_row][cur_col] = "*"
                cur_row -= 1
            else:
                continue
        elif direction == "right":
            if valid_index(cur_row, cur_col + 1):
                if field[cur_row][cur_col + 1] == "c":
                    coal_counter -= 1
                    if coal_counter == 0:
                        field[cur_row][cur_col] = "*"
                        cur_col += 1
                        break
                if field[cur_row][cur_col + 1] == "e":
                    field[cur_row][cur_col + 1] = "s"
                    print(f"Game over! ({cur_row}, {cur_col + 1})")
                    exit()
                field[cur_row][cur_col + 1] = "s"
                field[cur_row][cur_col] = "*"
                cur_col += 1
            else:
                continue
        elif direction == "down":
            if valid_index(cur_row + 1, cur_col):
                if field[cur_row + 1][cur_col] == "c":
                    coal_counter -= 1
                    if coal_counter == 0:
                        field[cur_row][cur_col] = "*"
                        cur_row += 1
                        break
                if field[cur_row + 1][cur_col] == "e":
                    field[cur_row + 1][cur_col] = "s"
                    print(f"Game over! ({cur_row + 1}, {cur_col})")
                    exit()
                field[cur_row + 1][cur_col] = "s"
                field[cur_row][cur_col] = "*"
                cur_row += 1
            else:
                continue

if coal_counter == 0:
    print(f"You collected all coals! ({cur_row}, {cur_col})")
else:
    print(f"{coal_counter} coals left. ({cur_row}, {cur_col})")
