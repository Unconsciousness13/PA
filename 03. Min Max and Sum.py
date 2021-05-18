def min_max_sum(nums):
    minimum = min(nums)
    maximum = max(nums)
    num_sum = sum(nums)
    print(f"The minimum number is {minimum}")
    print(f"The maximum number is {maximum}")
    print(f"The sum number is: {num_sum}")
    return maximum,minimum,num_sum


nums = [int(n) for n in input().split(" ")]
min_max_sum(nums)
