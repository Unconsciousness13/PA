from collections import deque


def palindrome(word_str, index=0):
    word = deque(word_str)
    while word:
        if len(word) == 1:
            word.pop()
            return f"{word_str} is a palindrome"

        first = word.popleft()
        last = word.pop()
        if first == last:
            palindrome(word)
        else:
            return f"{word_str} is not a palindrome"
    return f"{word_str} is a palindrome"


print(palindrome("abcba", 0))
