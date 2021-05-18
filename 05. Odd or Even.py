def odd_or_even(*args):
    if command == "Odd":
        result = [n for n in nums if n % 2 == 1]
        print(sum(result * len(nums)))
        return result
    elif command == "Even":
        result = [n for n in nums if n % 2 == 0]
        print(sum(result * len(nums)))
        return result


command = input()
nums = [int(n) for n in input().split(" ")]
odd_or_even(nums)
