# Basic Class and Object
# Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
my_car = Car("Toyota","Corolla")

print(my_car.brand) #Toyota
print(my_car.model) #Corolla

my_new_car = Car("Tata","Safari")
print(my_new_car.model) #Safari


#Add a method to the Car class that displays the full name of the car(brand and model)

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota","Corolla")

print(my_car.brand) #Toyota
print(my_car.model) #Corolla
print(my_car.full_name())  #Toyota Corolla