# names = input().split(', ')
# nam = []
# for name in names:
#     name_ = f"{name} -> {len(name)}"
#     nam.append(name_)
# print(", ".join(nam))

print(', '.join([f"{name} -> {len(name)}" for name in input().split(", ")]))
