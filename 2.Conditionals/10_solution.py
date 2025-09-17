#Pet Food Recommendation
# Problem - Recommend a type of food based on the pet's species and age (e.g., Dog: <2 years - Puppy food, Cat:>5 years - Senior Cat food)

# 
pet = input("Enter pet: ")
age = int(input("Enter age of pet : "))
if pet == "Dog":
    if age <2 :
        food = "Puppy Food"
    else:
        food = "Dog Food"

if pet == "Cat":
    if age > 5 :
        food = "Senior Cat Food"
    else:
        food = "Junior Cat Food"

    
print (food)