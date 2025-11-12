def merge_sort(orders):
    if len(orders) > 1:
        mid = len(orders) // 2
        L = orders[:mid]
        R = orders[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][1] < R[j][1]:
                orders[k] = L[i]
                i += 1
            else:
                orders[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            orders[k] = L[i]; i += 1; k += 1
        while j < len(R):
            orders[k] = R[j]; j += 1; k += 1

n = int(input("Enter number of orders: "))
orders = []
for i in range(n):
    t = int(input(f"Enter delivery time (min) for Order {i+1}: "))
    orders.append((f"Order {i+1}", t))

merge_sort(orders)
print("\nOrders sorted by delivery time:")
for o in orders:
    print(o[0], "->", o[1], "min")
