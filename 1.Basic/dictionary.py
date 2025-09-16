# chai_types ={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# print(chai_types) #{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
# print(chai_types["Masala"]) #Spicy
# #or 
# print(chai_types.get("Ginger")) #Zesty

# chai_types["Green"] = "Fresh"
# print(chai_types) #{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

# for chai in chai_types:
#     print(chai) #print key only not values

# for chai in chai_types:
#     print(chai,chai_types[chai]) #print keys and values both

# for key,value in chai_types.items():
#     print(key,value) #print keys and values both

# if "Masala" in chai_types:
#     print("I have masala chai") #I have masala chai

# print(len(chai_types)) #3

# print(chai_types.pop("Ginger")) #Zesty
# print(chai_types) #{'Masala': 'Spicy', 'Green': 'Fresh'}

# chai_types ={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# chai_types.popitem()
# print(chai_types) #{'Masala': 'Spicy', 'Ginger': 'Zesty'}
# print(chai_types)  ##{'Masala': 'Spicy', 'Green': 'Fresh'}


# del chai_types["Masala"]
# print(chai_types) #{'Ginger': 'Zesty'}

# tea_shop = {
#     "chai":{"Masala":"Spicy","Ginger":"Zesty"},
#     "Tea":{"Green":"Mild","Black":"Strong"}
# }
# print(tea_shop) #{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
# print(tea_shop["chai"]) #{'Masala': 'Spicy', 'Ginger': 'Zesty'}
# print(tea_shop["chai"]["Ginger"]) #Zesty

# squared_nums = {x:x**2 for x in range(6)}
# print(squared_nums) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# squared_nums.clear()
# print(squared_nums) #{}


# keys = ["Masala","Ginger","Lemon"]
# print(keys) #['Masala', 'Ginger', 'Lemon']
# default_value = "Delicious"
# new_dict = dict.fromkeys(keys,default_value)
# print(new_dict) #{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}

# new_dict = dict.fromkeys(keys,keys)
# print(new_dict) #{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
