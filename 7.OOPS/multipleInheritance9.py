#Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCar(Battery,Engine,Car):
    pass

my_newTesla= ElectricCar("Tesla","Model S")
print(my_newTesla.engine_info()) #this is engine
print(my_newTesla.battery_info()) #this is battery