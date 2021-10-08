"""
CP1404/CP5632 Practical
Car class
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        reliability_check = randint(1, 100)
        if self.reliability <= reliability_check:
            distance = 0

        distance_driven = super().drive(distance)

        return distance_driven
