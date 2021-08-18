matrix_size = int(input())
matrix = [[el for el in input().split()] for _ in range(matrix_size)]


def found_the_alice(row, col):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == alice:
                return row, col


def index_in_range(row_idx, col_idx):
    if 0 <= row_idx < len(matrix) and 0 <= col_idx < len(matrix):
        return True
    return False


alice = "A"
rabbit_hole = "R"
tea_bags = 0

delta_directions_path = {'up': (-1, 0), 'down': (+1, 0),
                         'left': (0, -1), 'right': (0, +1)}
alice_row = 0
alice_col = 0

while True:
    if tea_bags >= 10:
        print("She did it! She went to the party.")
        break
    direction = input()
    current_row, current_col = found_the_alice(alice_col, alice_col)
    next_row, next_col = current_row + delta_directions_path[direction][0], delta_directions_path[direction][
        1] + current_col

    if index_in_range(next_row, next_col):
        if matrix[next_row][next_col] == rabbit_hole:
            matrix[current_row][current_col] = "*"
            matrix[next_row][next_col] = "*"
            print("Alice didn't make it to the tea party.")
            break
        if matrix[next_row][next_col].isalnum():
            tea_bags += int(matrix[next_row][next_col])
            matrix[next_row][next_col] = alice
            matrix[current_row][current_col] = "*"
            if tea_bags >= 10:
                matrix[next_row][next_col] = "*"
        else:
            matrix[next_row][next_col] = alice
            matrix[current_row][current_col] = "*"
    else:
        matrix[current_row][current_col] = "*"
        print("Alice didn't make it to the tea party.")
        break

for el in matrix:
    print(" ".join(el))
