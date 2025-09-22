"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.max_cargo = max_cargo
        self.cargo = 0
        super().__init__(weight, fuel, fuel_consumption)

    def load_cargo(self, cargo):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        result = self.cargo
        self.cargo = 0
        return result