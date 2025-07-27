"""Test for UnreliableCar."""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test driving behavior of an UnreliableCar."""
    reliable_car = UnreliableCar("Reliable", 100, 90)  # 90% chance
    unreliable_car = UnreliableCar("Unreliable", 100, 10)  # 10% chance

    total_attempts = 100
    successful_reliable_drives = 0
    successful_unreliable_drives = 0

    for _ in range(total_attempts):
        if reliable_car.drive(1) > 0:
            successful_reliable_drives += 1
        if unreliable_car.drive(1) > 0:
            successful_unreliable_drives += 1

    print(f"ReliableCar successful drives: {successful_reliable_drives}/{total_attempts}")
    print(f"UnreliableCar successful drives: {successful_unreliable_drives}/{total_attempts}")


if __name__ == "__main__":
    main()