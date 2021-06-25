# checking if index is valid
def is_valid(current_row, current_col):
    if 0 <= current_row < len(darts_board) and 0 <= current_col < len(darts_board):
        return True
    return False


# finding current player
def player_turn(current_player):
    if (players_data[player1][0] + players_data[player2][0]) % 2 == 0:
        current_player = player1
    else:
        current_player = player2
    return current_player


# reading players names
player1, player2 = input().split(", ")

# players name [throws, score] ,using dictionary
players_data = {player1: [0, 501], player2: [0, 501]}

# read board
darts_board = [[el for el in input().split()] for r in range(7)]

while True:
    current_player = player_turn(players_data[player1][0] + players_data[player2][0])
    players_data[current_player][0] += 1

    # reading shoot indices
    shoots = input()
    shoots = shoots[1:len(shoots) - 1]
    row, col = [int(a) for a in shoots.split(", ")]

    # checking if the shoot is in range
    if is_valid(row, col):
        # making variables with the sum of indices
        double = ((int(darts_board[row][0])) + (int(darts_board[row][6])) + (int(darts_board[0][col])) + (
            int(darts_board[6][col]))) * 2
        triple = ((int(darts_board[row][0])) + (int(darts_board[row][6])) + (int(darts_board[0][col])) + (
            int(darts_board[6][col]))) * 3

        if darts_board[row][col] == "D":
            players_data[current_player][1] -= double

        elif darts_board[row][col] == "T":
            players_data[current_player][1] -= triple

        elif darts_board[row][col] == "B":
            print(f"{current_player} won the game with {players_data[current_player][0]} throws!")
            break

        else:
            players_data[current_player][1] -= int(darts_board[row][col])

        # Checking if the game is finished
        if players_data[current_player][1] <= 0:
            print(f"{current_player} won the game with {players_data[current_player][0]} throws!")
            break
