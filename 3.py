from collections import deque
text = input()
queue = deque([])
while not text == "End":
    if not text == "Paid":
        queue.append(text)

    if text == "Paid":
        for el in queue:
            print(el)
        queue = deque([])

    text = input()
print(f"{len(queue)} people remaining.")