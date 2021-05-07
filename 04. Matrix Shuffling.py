# rows, cols = [int(el) for el in input().split()]
#
#
# def init_matrix(rows, cols):
#     matrix = []
#     for _ in range(rows):
#         matrix.append(input().split())
#     return matrix
#
#
# def check_if_index_is_valid(index_row, index_col, rows, cols):
#     if 0 <= index_row < rows and 0 <= index_col < cols:
#         return True
#     return False
#
#
# def check_if_command_is_valid(command, coordinates, rows, cols):
#     if len(coordinates) == 4 and command == "swap":
#         for index in range(0, len(coordinates), 2):
#             if not check_if_index_is_valid(coordinates[index], coordinates[index + 1], rows, cols):
#                 print("Invalid input!")
#                 return False
#         return True
#     print("Invalid input!")
#     return False
#
#
# def print_matrix(matrix):
#     for row_index in range(0, len(matrix)):
#         for col_index in range(0, len(matrix[row_index])):
#             print(f"{matrix[row_index][col_index]}")
#         print()
#
#
# matrix = init_matrix(rows, cols)
# data = input()
# while not data == "END":
#     splitted_data = data.split()
#     try:
#         command = splitted_data[0]
#         coordinates = [int(el) for el in splitted_data[1:]]
#     except:
#         print("Invalid input!")
#     if check_if_command_is_valid(command, coordinates, rows, cols):
#         current_row = coordinates[0]
#         current_col = coordinates[1]
#         row_to_swap = coordinates[2]
#         col_to_swap = coordinates[3]
#         temp = matrix[current_row][current_col]
#         matrix[current_row][current_col] = matrix[row_to_swap][col_to_swap]
#         matrix[row_to_swap][col_to_swap] = temp
#         print_matrix(matrix)
#
#     data = input()
def is_valid(pos, rows, cols):
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

line = input().split()

while not line[0] == "END":
    if line[0] == "swap" and len(line) == 5:
        first_pos = [int(line[1]), int(line[2])]
        second_pos = [int(line[3]), int(line[4])]

        if is_valid(first_pos, rows, cols) and is_valid(second_pos, rows, cols):
            matrix[first_pos[0]][first_pos[1]], matrix[second_pos[0]][
                second_pos[1]] = matrix[second_pos[0]][second_pos[1]], \
                                 matrix[first_pos[0]][first_pos[1]]
            for row in matrix:
                print(" ".join(row))
        else:
            print('Invalid input!')

    else:
        print('Invalid input!')
    line = input().split()
