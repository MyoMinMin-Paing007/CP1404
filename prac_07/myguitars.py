from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    print("Add your own guitars!")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) != 3:  # skip blank or bad lines
                continue
            name, year, cost = parts
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars



def save_guitars(filename, guitars):
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_guitars(guitars):
    print("These are the guitars:")
    for i, guitar in enumerate(sorted(guitars), 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")


if __name__ == '__main__':
    main()
