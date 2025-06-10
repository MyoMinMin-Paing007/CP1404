"""
CP1404 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
"""
# Using f-string formatting to produce the output
guitar_name = "Gibson L-5 CES"
year = 1922
cost = 16036
print(f"{year} {guitar_name} for about ${cost:,.0f}!")

# Using a for loop with f-string formatting to produce the required output
for exponent in range(11):
    print(f"2 ^ {exponent:2} is {2 ** exponent:4}")
