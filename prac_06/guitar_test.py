from guitar import Guitar
#using get age method to test
guitar1 = Guitar("Gibson L-5 CES", 1922, 500)
guitar2 = Guitar("Another Guitar", 2013, 1000)
expected_age_gibson = 103
actual_age_gibson = guitar1.get_age()
print(f"{guitar1.name} get_age() - Expected {expected_age_gibson}. Got {guitar1.get_age()}")

expected_age_another = 12
actual_age_another = guitar2.get_age()
print(f"{guitar2.name} get_age() - Expected {expected_age_another}. Got {guitar2.get_age()}")

#Test the is_vintage method
expected_vintage_gibson = True
actual_vintage_gibson = guitar1.is_vintage()
print(f"Gibson L-5 CES is_vintage() - Expected {expected_vintage_gibson}. Got {actual_vintage_gibson}")

expected_vintage_another = False
actual_vintage_another = guitar2.is_vintage()
print(f"Another Guitar is_vintage() - Expected {expected_vintage_another}. Got {actual_vintage_another}")