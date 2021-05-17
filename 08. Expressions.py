# import itertools
#
# numbers = [n for n in input().split()]
# n = len(numbers)
# permutations = set(itertools.permutations(['-'] * n + ['+'] * n, n))
#
# for permutation in permutations:
#     expr = ''.join(itertools.chain(*zip(permutation, numbers)))
#     res = eval(expr)
#     print(f"{expr}={res}")

def expressions(nums, current_sum=0, expression=""):
    if not nums:
        return [(expression, current_sum)]

    result_plus = expressions(nums[1:], current_sum + nums[0], f"{expression}+{nums[0]}")
    result_minus = expressions(nums[1:], current_sum - nums[0], f"{expression}-{nums[0]}")
    return result_plus + result_minus


nums = [int(el) for el in input().split(', ')]
print(*[f"{el[0]}={el[1]}" for el in expressions(nums)], sep='\n')
