"""CP1404/CP5632 Practical - SilverServiceTaxi class."""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A more luxurious Taxi with higher fare based on fanciness and flagfall."""

    flagfall = 4.50  # Class variable for the extra charge per fare

    def __init__(self, name, fuel, fanciness):
        """
        Initialise a SilverServiceTaxi.

        :param name: str - Taxi name
        :param fuel: float - Initial fuel
        :param fanciness: float - Multiplier for price_per_km
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Use Taxi's class variable for base price, then scale it
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """
        Calculate fare including flagfall.

        :return: float - Total fare = base fare + flagfall
        """
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string representation with flagfall included."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    "prac09"