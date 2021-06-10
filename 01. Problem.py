from collections import deque

pizza_orders = deque([int(el) for el in input().split(", ")])
employees = deque([int(el) for el in input().split(", ")])

total_pizzas = 0

while True:
    if not pizza_orders:
        break
    if not employees:
        break
    for order in range(len(pizza_orders)):
        if pizza_orders[order] > 10 or pizza_orders[order] <= 0:
            pizza_orders.popleft()
            break
        if pizza_orders[order] > employees[-1]:
            total_pizzas += employees[-1]
            pizza_orders[order] -= employees[-1]
            employees.pop()

            break
        else:
            total_pizzas += pizza_orders[order]
            employees.pop()
            pizza_orders.popleft()
            break
if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(el) for el in employees])}")

if not employees:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in pizza_orders])}")
