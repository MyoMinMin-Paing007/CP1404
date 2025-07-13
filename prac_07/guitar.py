class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self):
        return self.get_age(2024) >= 50

    def __lt__(self, other):
        return self.year < other.year

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"


def run_tests():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Fender Stratocaster", 2014, 765.40)
    guitar3 = Guitar("Martin D-28", 1931, 12000.00)

    guitars = [guitar1, guitar2, guitar3]
    print(guitar1)
    print("Vintage guitars:")
    for guitar in guitars:
        if guitar.is_vintage():
            print(guitar.name)


if __name__ == "__main__":
    run_tests()
