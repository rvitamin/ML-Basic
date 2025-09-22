"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from engine import Engine


class Car(Vehicle):
    def set_engine(self, engine: Engine):
        self.engine = engine