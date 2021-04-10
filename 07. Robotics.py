from collections import deque
from datetime import datetime, timedelta

robots = input().split(';')

for i in range(len(robots)):
    robot = robots[i].split('-')
    robots[i] = {
        'name': robot[0],
        'processing_time': int(robot[1]),
        'available_at': 0
    }
# 8:00:00
start_time = datetime.strptime(input(), '%H:%M:%S')

items = deque()
next_item = input()
while not next_item == 'End':
    items.append(next_item)
    next_item = input()

current_time = 0

while items:
    current_time += 1

    next_item = items.popleft()

    for robot in robots:
        if robot['available_at'] <= current_time:
            robot['available_at'] = current_time + robot['processing_time'] 
            robot_name = robot['name']
            time_str = (start_time + timedelta(seconds=current_time)).strftime('%H:%M:%S')
            print(f'{robot_name} - {next_item} [{time_str}]')

            break

    else:
        items.append(next_item)