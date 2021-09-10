"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.name = "Big Red Car"
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)

    limo = Car(100)
    limo.name = "Limo"
    limo.add_fuel(20)

    limo.drive(115)
    print("odo =", limo.odometer)
    print(limo.name)

    print("{} {}, {}".format(my_car.name, my_car.fuel, my_car.odometer))
    print("{self.name} {self.fuel}, {self.odometer}".format(self=limo))


main()