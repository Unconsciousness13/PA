from collections import deque

firework_effects = deque([int(el) for el in input().split(", ")])
explosive_power = deque(int(el) for el in input().split(", "))

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

while True:
    if not firework_effects:
        break
    if not explosive_power:
        break
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        break
    for idx in range(len(firework_effects)):

        if firework_effects[idx] <= 0:
            firework_effects.popleft()
            break
        if explosive_power[-1] <= 0:
            explosive_power.pop()
            break
        if (firework_effects[idx] + explosive_power[-1]) % 5 == 0 and (firework_effects[idx] + explosive_power[
            -1]) % 3 == 0:
            crossette_fireworks += 1
            firework_effects.popleft()
            explosive_power.pop()
            break
        elif (firework_effects[idx] + explosive_power[-1]) % 3 == 0:
            palm_fireworks += 1
            firework_effects.popleft()
            explosive_power.pop()
            break
        elif (firework_effects[idx] + explosive_power[-1]) % 5 == 0:
            willow_fireworks += 1
            firework_effects.popleft()
            explosive_power.pop()
            break
        else:
            firework_effects[idx] -= 1
            if firework_effects[idx] > 0:
                firework_effects.append(firework_effects[idx])
                firework_effects.popleft()
                break
            else:
                firework_effects.popleft()
                break


if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
