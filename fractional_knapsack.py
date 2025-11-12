n = int(input("Enter number of parcels: "))
items = []
for i in range(n):
    w = float(input(f"Weight of parcel {i+1}: "))
    v = float(input(f"Profit of parcel {i+1}: "))
    items.append((v/w, w, v, i+1))

capacity = float(input("Enter truck capacity: "))

items.sort(reverse=True)
total_value = 0.0
for ratio, weight, value, id in items:
    if capacity <= 0:
        break
    if weight <= capacity:
        capacity -= weight
        total_value += value
        print(f"Parcel {id}: taken completely")
    else:
        fraction = capacity / weight
        total_value += value * fraction
        print(f"Parcel {id}: taken {fraction*100:.1f}%")
        capacity = 0

print(f"\nMaximum Profit: {total_value:.2f}")
