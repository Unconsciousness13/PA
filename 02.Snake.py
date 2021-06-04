def searching_for_the_snake(red, kolona):
    for r in range(len(new_matrix)):
        for c in range(len(new_matrix)):
            if new_matrix[r][c] == snake:
                red = r
                kolona = c
                break

    return red, kolona


def search_for_burrows(red, kolona):
    for r in range(len(new_matrix)):
        for c in range(len(new_matrix)):
            if new_matrix[r][c] == burrows:
                red = r
                kolona = c
                new_matrix[r][c] = snake
    return red, kolona


size = int(input())
matrix = [[el for el in input().split()] for x in range(size)]

snake = "S"
burrows = "B"
food_eaten = 0
snake_row = 0
snake_col = 0
new_matrix = []

for row in matrix:
    for l in row:
        new_matrix.append([x for x in l])

is_over = True

while is_over:
    if food_eaten >= 10:
        print("You won! You fed the snake.")
        is_over = False
        break

    command = input()

    if command == "left":
        snake_position = (searching_for_the_snake(snake_row, snake_col))
        red = snake_position[0]
        kolona = snake_position[1]
        if kolona <= 0:
            new_matrix[red][kolona] = "."
            is_over = False
            break
        if kolona > 0:
            if new_matrix[red][kolona - 1] == burrows:
                new_matrix[red][kolona] = "."
                new_matrix[red][kolona - 1] = "."
                search_for_burrows(red, kolona)
            if new_matrix[red][kolona - 1] == "*":
                food_eaten += 1
                new_matrix[red][kolona - 1] = snake
                new_matrix[red][kolona] = "."
            elif new_matrix[red][kolona - 1] == "-":
                new_matrix[red][kolona - 1] = snake
                new_matrix[red][kolona] = "."

    elif command == "right":
        snake_position = (searching_for_the_snake(snake_row, snake_col))
        red = snake_position[0]
        kolona = snake_position[1]
        if kolona >= size - 1:
            new_matrix[red][kolona] = "."
            is_over = False
            break
        if kolona < size - 1:
            if new_matrix[red][kolona + 1] == burrows:
                new_matrix[red][kolona] = "."
                new_matrix[red][kolona + 1] = "."
                search_for_burrows(red, kolona)
            if new_matrix[red][kolona + 1] == "*":
                food_eaten += 1
                new_matrix[red][kolona + 1] = snake
                new_matrix[red][kolona] = "."
            elif new_matrix[red][kolona + 1] == "-":
                new_matrix[red][kolona + 1] = snake
                new_matrix[red][kolona] = "."

    elif command == "down":
        snake_position = (searching_for_the_snake(snake_row, snake_col))
        red = snake_position[0]
        kolona = snake_position[1]
        if red >= size - 1:
            new_matrix[red][kolona] = "."
            is_over = False
            break
        if red < size - 1:
            if new_matrix[red + 1][kolona] == burrows:
                new_matrix[red][kolona] = "."
                new_matrix[red + 1][kolona] = "."
                search_for_burrows(red, kolona)
            if new_matrix[red + 1][kolona] == "*":
                food_eaten += 1
                new_matrix[red + 1][kolona] = snake
                new_matrix[red][kolona] = "."
            elif new_matrix[red + 1][kolona] == "-":
                new_matrix[red + 1][kolona] = snake
                new_matrix[red][kolona] = "."

    elif command == "up":
        snake_position = (searching_for_the_snake(snake_row, snake_col))
        red = snake_position[0]
        kolona = snake_position[1]
        if red <= 0:
            new_matrix[red][kolona] = "."
            is_over = False
            break
        if red > 0:
            if new_matrix[red - 1][kolona] == burrows:
                new_matrix[red][kolona] = "."
                new_matrix[red - 1][kolona] = "."
                search_for_burrows(red, kolona)
            if new_matrix[red - 1][kolona] == "*":
                food_eaten += 1
                new_matrix[red - 1][kolona] = snake
                new_matrix[red][kolona] = "."
            elif new_matrix[red - 1][kolona] == "-":
                new_matrix[red - 1][kolona] = snake
                new_matrix[red][kolona] = "."

if food_eaten < 10:
    print("Game over!")
print(f"Food eaten: {food_eaten}")
for el in new_matrix:
    print("".join(el))
