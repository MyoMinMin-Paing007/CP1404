"""Test program for the Taxi class."""

from prac_09.taxi import Taxi


def main():
    # Create a new taxi object (no need to pass price_per_km now)
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print the taxi's details and current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart the meter for a new fare
    my_taxi.start_fare()

    # Drive the taxi 100 km
    my_taxi.drive(100)

    # Print the taxi's details and current fare again
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()