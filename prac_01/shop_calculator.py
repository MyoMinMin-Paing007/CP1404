"""
CP1404 - Practical
"""
item_numbers = int(input("Enter items amount: "))
while item_numbers < 0:
    print("Invalid number of items!")
    item_numbers = int(input("Enter items amount: "))
total_price = 0
for i in range(item_numbers):
    items_price = float(input("Price of items: "))
    if items_price > 100:
        discount = items_price * 0.1
        items_price = items_price - discount
    total_price += items_price

print(f"Total Price for {item_numbers}items is ${total_price}")