from collections import deque

milligrams_caffeine = [int(m) for m in input().split(', ')]
drinks = deque([int(m) for m in input().split(', ')])

stamat_current_caffeine = 0

while True:
    if not milligrams_caffeine or not drinks:
        break
    current_milligrams_caffeine = milligrams_caffeine.pop()
    current_energy_drink = drinks.popleft()
    caffeine = current_milligrams_caffeine * current_energy_drink
    if caffeine + stamat_current_caffeine <= 300:
        stamat_current_caffeine += caffeine
    else:
        drinks.append(current_energy_drink)
        stamat_current_caffeine -= 30
        if stamat_current_caffeine < 0:
            stamat_current_caffeine = 0


if drinks:
    print(f"Drinks left: { ', '.join(map(str, drinks)) }")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_current_caffeine} mg caffeine.")