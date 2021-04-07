from collections import deque

peoples = deque(input().split(' '))
n_toss = int(input())

while len(peoples) > 1:
    peoples.rotate(-n_toss)
    loser = peoples.pop()
    print(f'Removed {loser}')
winner = peoples.pop()
print(f'Last is {winner}')
