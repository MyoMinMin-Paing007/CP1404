"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""
    "add name field to car class"
    def __init__(self, fuel=0,name="Car"):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self._odometer = 0
        self.name=name

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    """Adding __str__ method to car.py"""
    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"