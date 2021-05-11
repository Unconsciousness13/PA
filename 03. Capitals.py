cities = input().split(", ")
capitals = input().split(", ")
print(*[f"{cities[index]} -> {capitals[index]}" for index in range(len(cities))], sep="\n")
