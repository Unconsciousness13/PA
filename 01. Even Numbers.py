def even_nums(numbs):
    for n in nums:
        if n % 2 == 0:
            even.append(n)


nums = [int(n) for n in input().split(" ")]
even = []
even_nums(even)
print(even)
