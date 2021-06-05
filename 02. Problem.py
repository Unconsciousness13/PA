# reading the matrix
def read_matrix():
    matrix = [[x for x in input().split(" ")] for n in range(7)]
    return matrix


player_1_score = 501
player_2_score = 501
player_1, player_2 = input().split(", ")
turns_counter = -1
turns_counter_player_1 = 0
turns_counter_player_2 = 0

matrix = read_matrix()

while True:
    # Searching for shoots index
    shoots = input().split(", ")
    shoots_row, shoots_col = shoots[0][1], shoots[1][0]
    row = int(shoots_row)
    col = int(shoots_col)
    double = ((int(matrix[row][0])) + (int(matrix[row][6])) + (int(matrix[0][col])) + (
        int(matrix[6][col]))) * 2
    triple = ((int(matrix[row][0])) + (int(matrix[row][6])) + (int(matrix[0][col])) + (
        int(matrix[6][col]))) * 3
    turns_counter += 1
    # checking if the shoot is in range

    if turns_counter % 2 == 0:
        if 0 <= row < 7 and 0 <= col < 7:
            turns_counter_player_1 += 1
            if matrix[row][col].isnumeric():
                player_1_score -= int(matrix[row][col])
            elif matrix[row][col] == "D":
                player_1_score -= double
            elif matrix[row][col] == "T":
                player_1_score -= triple
            elif matrix[row][col] == "B":
                print(f"{player_1} won the game with {turns_counter_player_1} throws!")
                break
            if player_1_score <= 0:
                print(f"{player_1} won the game with {turns_counter_player_1} throws!")
                break
        else:
            turns_counter_player_1 += 1
            player_1_score += 0

    else:
        if 0 <= row < 7 and 0 <= col < 7:
            turns_counter_player_2 += 1
            if matrix[row][col].isnumeric():
                player_2_score -= int(matrix[row][col])
            elif matrix[row][col] == "D":
                player_2_score -= double
            elif matrix[row][col] == "T":
                player_2_score -= triple
            elif matrix[row][col] == "B":
                print(f"{player_2} won the game with {turns_counter_player_2} throws!")
                break
            if player_2_score <= 0:
                print(f"{player_2} won the game with {turns_counter_player_2} throws!")
                break
        else:
            turns_counter_player_2 += 1
            player_2_score += 0


