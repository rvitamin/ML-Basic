from abc import ABC
from exceptions import (
    LowFuelError,
    NotEnoughFuel,
)


class Vehicle(ABC):
    def __init__(self, weight=1000, fuel=50, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.started == False and self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError()

    def move(self, distance):
        if self.started == False and self.fuel > distance/self.fuel_consumption:
            self.fuel -= distance/self.fuel_consumption
        else:
            raise NotEnoughFuel()