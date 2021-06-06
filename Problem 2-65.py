def read_matrix():
    matrix = [[i for i in input().split(" ")] for el in range(n)]
    return matrix


def searching_for_the_player(row, col):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "P":
                row = r
                col = c
                break

    return row, col


def check_index(index):
    if 0 < index < len(matrix):
        return True
    return False


n = int(input())
matrix = read_matrix()

r = 0
c = 0
player = searching_for_the_player(r, c)
player_row = player[0]
player_col = player[1]

coins = 0

out_index = False

while True:
    command = input()
    if command == "right":
        if player_col + 1 > n - 2:
            out_index = True
            break

    elif command == "left":
        pass
    elif command == "up":
        pass
    elif command == "down":
        pass
    else:
        continue

if out_index:
    print(f"Game over! You've collected {coins} coins.")