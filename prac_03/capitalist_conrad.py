"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

# Constants
FILENAME = "stock_prices.txt"
INITIAL_PRICE = 10.00
MIN_PRICE = 1.00
MAX_PRICE = 100.00
MAX_INCREASE = 0.175  # 17.5% increase
MAX_DECREASE = 0.05  # 5% decrease

# Initialize variables
price = INITIAL_PRICE
number_of_days = 0

# Open file for writing
out_file = open(FILENAME, 'w')

# Print and write the starting price
print(f"Starting price: ${price:,.2f}")
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate stock price changes
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    change = random.uniform(0, MAX_INCREASE) if random.randint(0, 1) else -random.uniform(0, MAX_DECREASE)
    price += price * change
    print(f"On day {number_of_days} price is: ${price:,.2f}")
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()


