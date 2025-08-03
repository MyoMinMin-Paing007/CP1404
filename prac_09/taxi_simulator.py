"""Taxi Simulator - CP1404"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def display_menu():
    print("q)uit, c)hoose taxi, d)rive")


def list_taxis(taxis):
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    display_menu()
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            list_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    total_bill += trip_cost
                except ValueError:
                    print("Invalid distance")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        display_menu()
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    list_taxis(taxis)


if __name__ == '__main__':
    main()