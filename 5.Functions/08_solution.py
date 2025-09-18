#function with **kwargs
#Create a function that accepts any number of keyword arguments and prints them in the format => key:value

# def print_kwargs(name,power):
#     print("Name: ",name, "Power: ",power)
# print_kwargs(name="Shaktiman",power="lazer") #Name:  Shaktiman Power:  lazer
# print_kwargs(power="lazer",name="Shaktiman") #Name:  Shaktiman Power:  lazer
# print_kwargs(name="Shaktiman",power="lazer",enemy="Dr. Jackal")  #TypeError: print_kwargs() got an unexpected keyword argument 'enemy'
# print_kwargs(name="Shaktiman") #NameError: name 'print_kwargs' is not defined

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
print_kwargs(name="Shaktiman",power="lazer") #name:  Shaktiman power:  lazer
print_kwargs(power="lazer",name="Shaktiman") #name:  Shaktiman power:  lazer
print_kwargs(name="Shaktiman",power="lazer",enemy="Dr. Jackal")  #name:  Shaktiman power:  lazer enemy: Dr. Jackal
print_kwargs(name="Shaktiman") #name:  Shaktiman