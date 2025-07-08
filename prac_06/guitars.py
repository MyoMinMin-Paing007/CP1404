from guitar import Guitar

print("My guitars!")
guitars = []

# get name
name = input("Name: ")

# Only enter loop if name is not empty
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")

    # Ask again at the end of the loop
    name = input("Name: ")

# using is_vintage and loop through the list
print("\nThese are my guitars:")

for guitar in guitars:
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    else:
        vintage_string=""
    print(f"{guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")