#Add a Static method to the Car class that return a general description of a Car


# class Car:
#     total_car = 0
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#         Car.total_car +=1
        
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
    
#     def general_description(self):
#         return "Cars are mean of transportation"

# safari = Car("Tata","Safari")
# safariTwo = Car("Tata","Nexon")
# print(safari.general_description())
# print(Car.general_description()) #TypeError: Car.general_description() missing 1 required positional argument: 'self'


#Add a Static method to the Car class that return a general description of a Car

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car +=1
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    @staticmethod
    def general_description(): #no need to pass self while using self method
        return "Cars are mean of transportation"

safari = Car("Tata","Safari")
safariTwo = Car("Tata","Nexon")
print(safari.general_description())#Cars are mean of transportation  
print(Car.general_description()) #Cars are mean of transportation  
