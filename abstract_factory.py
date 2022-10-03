from __future__ import annotations
from abc import abstractmethod, ABC


class Laptop(ABC):
    @abstractmethod
    def purchase(self):
        pass 


class MobilePhone(ABC):
    @abstractmethod
    def purchase(self):
        pass 

 
class AppleLaptop(Laptop):
    def purchase(self):
        print("You purchased apple's laptop")


class SamsungLaptop(Laptop):
    def purchase(self):
        print("You purchased samsung's laptop")


class AppleMobile(MobilePhone):
    def purchase(self):
        print("You purchased iPhone 14")


class SamsungMobile(MobilePhone):
    def purchase(self):
        print("You purchased galaxy s22")


class DeviceFactory(ABC):
    @abstractmethod
    def create_laptop(self):
        pass 

    @abstractmethod
    def create_mobile(self):
        pass 


class AppleFactory(DeviceFactory):
    def create_laptop(self):
        return AppleLaptop()
    def create_mobile(self):
        return AppleMobile()

class SamsungFactory(DeviceFactory):
    def create_laptop(self):
        return SamsungLaptop()
    def create_mobile(self):
        return SamsungMobile()

def main():
    applyFactory = AppleFactory()
    iphone = applyFactory.create_mobile().purchase()
    macbook = applyFactory.create_laptop().purchase()

    samsungFactory = SamsungFactory()
    samsung_galaxy = samsungFactory.create_mobile().purchase()
    samsung_laptop = samsungFactory.create_laptop().purchase()

    
if __name__ == "__main__":
    main()