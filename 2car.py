size = int(input())
race_number = int(input())
race_circuit = []
for _ in range(size):
    race_circuit.append(input().split())

tunel = 'T'
finish = 'F'
car = 'C'
km_covered = 0

directions = {'up': (-1, 0), 'down': (+1, 0),
              'left': (0, -1), 'right': (0, +1)}


def searching_for_tunel_exit(circuit):
    for row in range(len(circuit)):
        for col in range(len(circuit[0])):
            if circuit[row][col] == tunel:
                return row, col

current_row = 0
current_col = 0
race_circuit[0][0] = car

while True:
    command = input()

    if command == 'End':
        race_circuit[current_row][current_col] = car
        print(f"Racing car {race_number} DNF.")
        break

    if command in directions:
        next_row, next_col = current_row + \
            directions[command][0], directions[command][1] + current_col
        race_circuit[current_row][current_col] = '.'
        km_covered += 10
        if race_circuit[next_row][next_col] == tunel:
            race_circuit[next_row][next_col] = '.'
            next_row,next_col = searching_for_tunel_exit(race_circuit)
            km_covered += 20
        elif race_circuit[next_row][next_col] == finish:
            race_circuit[next_row][next_col] = car
            print(f"Racing car {race_number:02d} finished the stage!")
            break
        current_row = next_row
        current_col = next_col
        race_circuit[next_row][next_col] = car







print(f"Distance covered {str(km_covered).zfill(2)} km.")
for row in range(len(race_circuit)):
    print("".join(race_circuit[row]))