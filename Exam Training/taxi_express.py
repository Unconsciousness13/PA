from collections import deque

customers = deque([int(cus) for cus in input().split(", ")])
taxis = deque([int(taxi) for taxi in input().split(",")])

total_time = 0

while customers and taxis:
    customer = customers[0]
    taxi = taxis[-1]
    if taxi >= customer:
        total_time += customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

else:
    print("Not all customers were driven to their destinations")
    print(f'Customers left: {", ".join(map(str, customers))}')
