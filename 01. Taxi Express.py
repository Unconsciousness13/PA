from collections import deque

customers = [int(el) for el in input().split(", ")]
taxis = [int(el) for el in input().split(", ")]

customers_queue = deque(customers)
taxis = deque(taxis)

time_driven = 0
while customers_queue:

    for customer in customers_queue:
        if customer <= taxis[-1]:
            time_driven += customer
            taxis.pop()
            customers_queue.popleft()
            break
        else:
            taxis.pop()
            break
    if not taxis:
        break
if not customers_queue:
    print("All customers were driven to their destinations")
    print(f"Total time: {time_driven} minutes")
if not taxis and customers_queue:
    res = [str(a) for a in customers_queue]
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(res)}")
