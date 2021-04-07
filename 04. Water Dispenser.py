from collections import deque

liters_in_dispenser = int(input())
peoples = deque([])
while True:
    command = input()
    if command == "Start":
        break
    else:
        name = command
        peoples.append(name)
while True:
    command = input()
    if command == "End":
        break
    elif command.isnumeric():
        litters_to_drink = int(command)
        person = peoples.popleft()
        if liters_in_dispenser >= litters_to_drink:
            print(f"{person} got water")
            liters_in_dispenser -= litters_to_drink
        else:
            print(f"{person} must wait")
    elif command.startswith("refill"):
        litters_to_add = int(command.split(" ")[-1])
        liters_in_dispenser += litters_to_add
print(f"{liters_in_dispenser} liters left")
