"""The Abstract Factory Pattern"""

# Libraries
from abc import ABCMeta, abstractmethod


class Car(metaclass=ABCMeta):
    def __init__(self):
        self.name = None
        self.max_speed = None

    def __str__(self):
        return "name is {} and the velocity {}".format(
            self.name,
            self.max_speed
        )


class SportsCar(Car):
    def __init__(self):
        self.name = "Sports"
        self.max_speed = '300km/h'


class FamilyCar(Car):
    def __init__(self):
        self.name = "Familiar"
        self.max_speed = '100km/h'


class AbstractFactory(metaclass=ABCMeta):
    def __init__(self):
        self.manufacturer = None

    def __str__(self):
        return 'Manufacturer - {}'.format(self.manufacturer)

    @abstractmethod
    def create_car(self, car_type):
        pass

    @staticmethod
    def get_factory(factory_name):
        if factory_name == 'vw':
            return VWFactory()
        raise TypeError('Undefined Factory')


class VWFactory(AbstractFactory):
    def __init__(self):
        self.manufacturer = 'vw'

    def create_car(self, car_type):
        self.car = None
        if car_type == 'sports':
            self.car = SportsCar()
        if car_type == 'family':
            self.car = FamilyCar()
        return self.car

    def do_something(self):
        print(self.car)


class MyFactory:
    def __init__(self):
        pass

    def create_car(self, car_type):
        self.car = None
        if car_type == 'sports':
            self.car = SportsCar()
        if car_type == 'family':
            self.car = FamilyCar()
        return self.car

    def do_something(self):
        print(self.car)


if __name__ == '__main__':
    myfac = MyFactory()
    s = myfac.create_car('sports')
    f = myfac.create_car('family')

    print(s)
    print(f)

    abstract_factory = AbstractFactory.get_factory('vw')

    print(abstract_factory)

    s = abstract_factory.create_car('sports')
    f = abstract_factory.create_car('family')

    print(s)
    print(f)
