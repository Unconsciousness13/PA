heroes = {hero: [] for hero in input().split(", ")}

data = input()
while not data == "End":
    hero, item, price = data.split("-")
    if item not in heroes[hero]:
        heroes[hero] += [item, price]
    data = input()

for hero, items in heroes.items():
    cost = [int(item) for item in items if item.isdecimal()]
    print (f"{hero} -> Items: {int(len(items) / 2)}, Cost: {sum(cost)}")