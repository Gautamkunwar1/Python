# tea_varities = ["Black","Green","Oolong","White"]
# print(tea_varities[0]) #Black
# print(tea_varities[1:3]) # ['Green', 'Oolong']
# tea_varities[3] = "Herbal"
# print(tea_varities) #['Black', 'Green', 'Oolong', 'Herbal']
# tea_varities[1:2] = "Lemon"
# print(tea_varities) #['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
# tea_varities = ["Black","Green","Oolong","White"]
# tea_varities[1:2] = ["Lemon"]
# print(tea_varities) #['Black', 'Lemon', 'Oolong', 'White']
# print(tea_varities[1:1]) #[]
# tea_varities[1:1] =["test","test"]
# print(tea_varities) #['Black', 'test', 'test', 'Lemon', 'Oolong', 'White']
# tea_varities[1:3] = []
# print(tea_varities) #['Black', 'Lemon', 'Oolong', 'White']

# for tea in tea_varities:
#     print(tea, end="-") #Black-Lemon-Oolong-White-

# if "Oolong" in tea_varities:
#     print("I have Oolong tea") #-I have Oolong tea


# tea_varities.append("Lemon")
# print(tea_varities) #['Black', 'Green', 'Oolong', 'White', 'Lemon']
# print(tea_varities.pop()) #Lemon
# tea_varities.remove("Oolong")
# print(tea_varities) #['Black', 'Green', 'White'] 
# tea_varities.insert(1,"Elaichi")
# print(tea_varities) #['Black', 'Elaichi', 'Green', 'White']

# squared_num = [x**2 for x in range(10)]
# print(squared_num) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# cube_nums = [x**3 for x in range(5)]
# print(cube_nums) #[0, 1, 8, 27, 64]