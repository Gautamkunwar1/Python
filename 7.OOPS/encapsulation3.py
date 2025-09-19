class Car:
    def __init__(self,brand,model):
        self.__brand = brand #__ makes private
        self.model = model
    
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
my_car = Car("Toyota","Corolaa")
#print(my_car.brand) #AttributeError: 'Car' object has no attribute 'brand'
print(my_car.get_brand()) #Toyota !

