from collections import deque

bomb_effects = [int(i) for i in input().split(", ")]
bomb_casing = [int(b) for b in input().split(", ")]
bomb_effects = deque(bomb_effects)
bomb_casing = deque(bomb_casing)

datura_bombs = 40
cherry_bombs = 60
smoke_dekoy_bombs = 120

datura_bomb_count = 0
cherry_bomb_count = 0
smoke_bomb_count = 0

while bomb_effects and bomb_casing:
    if datura_bomb_count >= 3 and cherry_bomb_count >= 3 and smoke_bomb_count >= 3:
        break
    current_effect = bomb_effects[0]
    current_casing = bomb_casing[-1]

    if current_effect + current_casing == datura_bombs:
        datura_bomb_count += 1
        bomb_effects.popleft()
        bomb_casing.pop()

    elif current_effect + current_casing == cherry_bombs:
        cherry_bomb_count += 1
        bomb_effects.popleft()
        bomb_casing.pop()
    elif current_effect + current_casing == smoke_dekoy_bombs:
        smoke_bomb_count += 1
        bomb_effects.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5

if datura_bomb_count >= 3 and cherry_bomb_count >= 3 and smoke_bomb_count >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(el) for el in bomb_casing])}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bomb_count}")
print(f"Datura Bombs: {datura_bomb_count}")
print(f"Smoke Decoy Bombs: {smoke_bomb_count}")
