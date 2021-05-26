n, m = [int(num) for num in input().split(" ")]
one = set()
two = set()
for _ in range(n):
    nums = input()
    one.add(nums)
for _ in range(m):
    nums = input()
    two.add(nums)
result = one.intersection(two)
for el in result:
    print(el)
