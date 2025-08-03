"""CP1404/CP5632 Practical - UnreliableCar class."""

import random
from prac_09.car import Car


class UnreliableCar(Car):
    """A Car that may not always drive depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """
        Initialise an UnreliableCar instance.

        :param name: str - Car name
        :param fuel: float - Initial fuel
        :param reliability: float (0–100) - Chance the car will successfully drive
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Attempt to drive the car based on its reliability.

        Only drive if a random number is less than the car's reliability.
        Return the distance actually driven (0 if it fails).
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0  # Car failed to drive this time