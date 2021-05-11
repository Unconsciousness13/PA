# def read_matrix():
#     row_counts = int(input())
#     return [[int(x) for x in input().split(", ")] for _ in range(row_counts)]
#
#
# matrix = read_matrix()
# print([x for row in matrix for x in row])
#

# with functions
def read_matrix():
    rows_count = int(input())
    return [input().split(', ') for _ in range(rows_count)]


def flatten(matrix):
    return [x for row in matrix for x in row]


def print_result(values):
    print([int(x) for x in values])


matrix = read_matrix()
result = flatten(matrix)
print_result(result)
