from collections import deque
peoples = deque()
while True:
    command = input()
    if command == 'Paid':
        while len(peoples) > 0:
            print(peoples.popleft())
    elif command == 'End':
        break
    else:
        name = command
        peoples.append(name)
print(f'{len(peoples)} people remaining.')