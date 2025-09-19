
#Create an Electric Car that inherits from the Car class and has an additional attribute battery_size

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self,brand,model, battery_size):
        super().__init__(brand,model) # super => apne se upr or uske init method ka access
        self.battery_size = battery_size
        
my_tesla = ElectricCar("Tesla","Model S", "85 kWh")
# print(my_tesla.model) #Model S
# print(my_tesla.full_name()) #Tesla Model S


#Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and Electric Car
print(isinstance(my_tesla,Car)) #True
print(isinstance(my_tesla,ElectricCar)) #True