from collections import deque

total_quantity = int(input())

orders_queue = deque(map(int, input().split(' ')))

print(max(orders_queue))

while orders_queue:
    # take first order
    order = orders_queue.popleft()

    # check if we have any quantity left
    if total_quantity >= order:
        #remove from total quantity
        total_quantity -= order
    else:
        # order > total_quantity
        orders_queue.appendleft(order)
        break
if orders_queue:
    # TODO print remaning orders
    orders_left = ' '.join(list(map(lambda x: str(x), orders_queue)))
    print(f'Orders left {orders_left}')
else:
    print('Orders complete')