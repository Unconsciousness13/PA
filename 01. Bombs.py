from collections import deque

bomb_effects = deque(int(el) for el in input().split(", "))
bomb_casing = deque(int(el) for el in input().split(", "))
queue = []
for el in range(len(bomb_casing)):
    queue.append(bomb_casing.pop())

datura_bombs = 40
cherry_bombs = 60
smoke_decoy_bombs = 120

cherry_count = 0
datura_count = 0
smoke_count = 0

while True:
    i = 0

    if bomb_effects[i] + queue[i] == datura_bombs:
        datura_count += 1
        bomb_effects.popleft()
        queue.pop(i)
    elif bomb_effects[i] + queue[i] == cherry_bombs:
        cherry_count += 1
        bomb_effects.popleft()
        queue.pop(i)
    elif bomb_effects[i] + queue[i] == smoke_decoy_bombs:
        smoke_count += 1
        bomb_effects.popleft()
        queue.pop(i)
    else:
        queue[i] -= 5

    if len(queue) < 1 or len(bomb_effects) < 1:
        print("You don't have enough materials to fill the bomb pouch.")
        break
    if 2 < datura_count and 2 < cherry_count and 2 < smoke_count:
        print("Bene! You have successfully filled the bomb pouch!")
        break
de = list(bomb_effects)
if bomb_effects:
    print(f"Bomb Effects: ", end="")
    print(', '.join(map(str, de)))

else:
    print("Bomb Effects: empty")
if queue:
    print(f"Bomb Casings: ", end="")
    print(', '.join(map(str, queue)))

else:
    print("Bomb Casings: empty")
print(f"Cherry Bombs: {cherry_count}")
print(f"Datura Bombs: {datura_count}")
print(f"Smoke Decoy Bombs: {smoke_count}")
