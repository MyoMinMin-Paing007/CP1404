"""Test SilverServiceTaxi functionality."""

from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi: name="Hummer", fuel=200, fanciness=2
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Start a new fare and drive 18 km
    fancy_taxi.start_fare()
    fancy_taxi.drive(18)

    # Check fare should be: (18 * 2 * 1.23) + 4.50 = 48.78
    expected_fare = 48.78
    actual_fare = fancy_taxi.get_fare()

    print(f"TAXI: {fancy_taxi}")
    print(f"Expected Fare: ${expected_fare:.2f}")
    print(f"Actual Fare:   ${actual_fare:.2f}")

    # Assert for correctness (will raise AssertionError if wrong)
    assert abs(actual_fare - expected_fare) < 0.05, "Fare calculation is incorrect."


if __name__ == "__main__":
    main()