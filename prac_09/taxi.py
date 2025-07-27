"""CP1404/CP5632 Practical - Taxi class."""

from prac_09.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare calculation."""

    price_per_km = 1.23  # Class variable used as base fare rate

    def __init__(self, name, fuel):
        """
        Initialise a Taxi instance.

        :param name: str - Taxi name
        :param fuel: float - Initial fuel
        """
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def start_fare(self):
        """Reset the current fare distance for a new fare."""
        self.current_fare_distance = 0

    def get_fare(self):
        """
        Calculate the fare for the current trip.

        The fare is calculated as distance × price_per_km,
        then rounded to the nearest 10 cents (0.1).
        This is to reflect real-world pricing practice.

        :return: float - Total fare, rounded to nearest 10c
        """
        raw_fare = self.price_per_km * self.current_fare_distance
        return round(raw_fare, 1)

    def drive(self, distance):
        """
        Drive the Taxi, tracking fare distance as well as fuel usage.

        :param distance: float - Distance to drive
        :return: float - Distance actually driven
        """
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

    def __str__(self):
        """Return string representation including fare distance and price."""
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km")