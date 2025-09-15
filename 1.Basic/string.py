# chai = "Masala Chai"
# print(chai[0]) #M

# slice_chai = chai[0:6]
# print(slice_chai) #Masala
# print(chai[-1]) #i

# num_list="0123456789"
# print(num_list[:]) # 0123456789
# print(num_list[3:]) #3456789
# print(num_list[:7]) #0123456
# print(num_list[0:7:2]) #0246
# print(num_list[0:7:3]) #036

# chai="Masala Chai"
# print(chai.lower()) #masala chai
# print(chai.upper()) #MASALA CHAI


# chai="  Masala Chai  "
# print(chai) #  Masala Chai  
# print(chai.strip()) #Masala Chai => strip() removes whitespace

# chai = "Lemon Chai"
# print(chai.replace("Lemon","Ginger")) #Ginger Chai

# chai="Masala Chai"
# print(chai.find("Chai")) #7

# chai= "Lemon, Ginger, Masala, Mint"
# print(chai.split()) #['Lemon,', 'Ginger,', 'Masala,', 'Mint']
# print(chai.split(", ")) #['Lemon', 'Ginger', 'Masala', 'Mint']

# chai="Masala Chai Chai Chai"
# print(chai.count("Chai")) #3

# chai = "Masala"
# quantity = 2
# order = "I ordered {} copy of {} chai"
# print(order) #I ordered {} copy of {} chai

# print(order.format(quantity,chai)) #I ordered 2 copy of Masala chai

# #list to string
# chai_variety= ["lemon","masala",'ginger']
# print("".join(chai_variety))  #lemonmasalaginger
# print(" ".join(chai_variety))  #lemon masala ginger
# print("-".join(chai_variety))  #lemon-masala-ginger

# chai="Masala Chai"
# print(len(chai)) #11

# for letter in chai:
#     print(letter) 

# chai="He said,\"Masala Chai is awesome\" "
# print(chai) # He said,"Masala Chai is awesome" 

# chai = r"Masala\nchai"
# print(chai) #Masala\nchai

# chai=r"C:\user\pwd"
# print(chai) # C:\user\pwd

# chai= "Masala Chai"
# print("Masala" in chai) #True
# print("masala" in chai) #False