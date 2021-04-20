repetitions = int(input())

my_names = set()

for num in range(repetitions):
    name = input()
    my_names.add(name)
for _ in my_names:
    print(_)