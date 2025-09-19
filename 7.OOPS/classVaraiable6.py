# #Class Variable
# #Add a class variable to Car that keeps track of the number of cars created

# class Car:
#     total_car = 0
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#         # self.total_car +=1
#         Car.total_car +=1
        
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
# safari = Car("Tata","Safari")
# safariTwo = Car("Tata","Nexon")
# print(safari.model) #Safari
# print(safariTwo.model) #Nexon
# print(safari.total_car) #2
# # test = Car("test","test")
# # print(test.total_car) #3

# print(Car.total_car) #2


#Class Variable
#Add a class variable to Car that keeps track of the number of cars created

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        # self.total_car +=1
        Car.total_car +=1
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
Car("Tata","Safari")
Car("Tata","Nexon")
print(Car.total_car) #2