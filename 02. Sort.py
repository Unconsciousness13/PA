def sort_list(nums):
    result = list(num for num in nums)
    return result


nums = [int(n) for n in input().split(" ")]
sor_res = sorted(sort_list(nums), key=lambda x: x)

print(sor_res)
