def positive(nums):
    positives = [n for n in nums if n >= 0]
    return positives


def negative(nums):
    negatives = [n for n in nums if n < 0]
    return negatives


nums = [int(n) for n in input().split(" ")]
print(sum(negative(nums)))
print(sum(positive(nums)))
negative_abs = abs(sum(negative(nums)))
if negative_abs > sum(positive(nums)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


