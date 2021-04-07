from collections import deque

peoples = deque()
while True:
    command = input()
    if command == 'Paid':
        peoples_who_paid = [peoples.popleft() for _ in range(len(peoples))]
        print('\n'.join(peoples_who_paid))
    elif command == 'End':
        break
    else:
        name = command
        peoples.append(name)
print(f'{len(peoples)} people remaining.')
