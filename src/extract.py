import csv

orders = []

with open("data/raw/orders.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        orders.append(row)

    
second_order = orders[1]

quantity = int(second_order["quantity"])
unit_price = float(second_order["unit_price"])

order_total = quantity * unit_price
print(f"Order Total: ${order_total:.2f}")


for order in orders:
    order["quantity"] = int(order["quantity"])
    order["unit_price"] = float(order["unit_price"])