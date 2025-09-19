#Use a property Decorator in the Car class to make the model readonly

# class Car:
#     total_car = 0
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#         Car.total_car +=1
        
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     @staticmethod
#     def general_description(): 
#         return "Cars are mean of transportation"

# safari = Car("Tata","Safari")
# safari.model = "City"
# print(safari.model) #City

# safariTwo = Car("Tata","Nexon")
# print(safari.general_description())#Cars are mean of transportation  
# print(Car.general_description()) #Cars are mean of transportation  



# class Car:
#     total_car = 0
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.__model = model
#         Car.total_car +=1
        
#     def full_name(self):
#         return f"{self.brand} {self.__model}"
    
#     @staticmethod
#     def general_description(): 
#         return "Cars are mean of transportation"
    
#     def model(self):
#         return self.__model

# safari = Car("Tata","Safari")
# safari.model = "City"
# print(safari.model) #City
# print(safari.model()) #TypeError: 'str' object is not callable

# safariTwo = Car("Tata","Nexon")


class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model
        Car.total_car +=1
        
    def full_name(self):
        return f"{self.brand} {self.__model}"
    
    @staticmethod
    def general_description(): 
        return "Cars are mean of transportation"
    
    @property
    def model(self):
        return self.__model

safari = Car("Tata","Safari")
# safari.model = "City"
# print(safari.model) #AttributeError: property 'model' of 'Car' object has no setter
print(safari.model)  #Safari

safariTwo = Car("Tata","Nexon")