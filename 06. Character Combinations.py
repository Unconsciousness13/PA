# permutation = set()

def print_combination(text, index):
    if index >= len(text):
        print(''.join(text))
        return
    print_combination(text, index + 1)
    for i in range(index + 1, len(text)):
        text[index], text[i] = text[i], text[index]
        print_combination(text, index + 1)
        text[index], text[i] = text[i], text[index]


# def generate(k: int, A: list):
#     if k == 1:
#         permutation.add(''.join(A))
#     else:
#         generate(k - 1, A)
#
#         for i in range(k):
#             if k % 2 == 0:
#                 A[i], A[k - 1] = A[k - 1], A[i]
#             else:
#                 A[0], A[k - 1] = A[k - 1], A[0]
#
#             generate(k - 1, A)


# s = list(input())
# # generate(len(s), s)
# # print('\n'.join(list(permutation)))
text = list(input())
print_combination(text, 0)
