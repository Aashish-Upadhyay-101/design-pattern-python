
from abc import ABC, abstractmethod


class VehicleBuilder(ABC):
    @property
    @abstractmethod
    def vehicle_type(self):
        pass 

    @abstractmethod
    def wheel_no(self, number):
        pass 

    @abstractmethod
    def build_design(self, design):
        pass 

    @abstractmethod
    def build_engine(self, engine):
        pass 


class AutomobileFactory(VehicleBuilder):

    def __init__(self):
        self.set_type()

    def set_type(self):
        self._type = Car() 

    def vehicle_type(self):
        type = self._type 
        return type

    def wheel_no(self, number):
        self._type.number_of_wheels = number 

    def build_design(self, design):
        self._type.design = design

    def build_engine(self, engine):
        self._type.engine = engine


class CarShowroom:
    def __init__(self):
        self._factory = None 

    @property
    def factory(self) -> AutomobileFactory:
        return self._factory

   
    def factory(self, factory: VehicleBuilder) -> None:
        self._factory = factory

    def order_car(self):
        self._factory.wheel_no(4)
        self._factory.build_design("Slick")
        self._factory.build_engine("6600 HP")

class Car:
    def __init__(self):
        self.number_of_wheels: int 
        self.design: str
        self.engine: str 

    def ready_car(self):
        print(self.number_of_wheels, self.design, self.engine)


def main():
    showroom = CarShowroom()
    factory = AutomobileFactory()

    showroom._factory = factory
    showroom.order_car()
    
    factory._type.ready_car()


if __name__ == "__main__":
    main()


