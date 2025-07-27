class Car:
    """A simple Car class."""

    def __init__(self, name, fuel):
        """Initialise a Car instance."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def drive(self, distance):
        """Drive the car a given distance."""
        if distance > self.fuel:
            distance = self.fuel
        self.fuel -= distance
        self.odometer += distance
        return distance
