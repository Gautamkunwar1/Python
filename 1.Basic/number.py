# x =2
# print(x)
# print(40 +2.23)
# print(float(40) + 2.23) #Good practice


# print(2**100) #1267650600228229401496703205376

# x = 2
# y = 3
# z = 5
# print(x, y, z)
# print(x<y<z)
# print (x<y and y<z) #both line are same

# import math
# # floor brings closest no. below value
# print(math.floor(3.5)) #3
# print(math.floor(-3.5)) #-4
# # trunc brings toward zero
# print(math.trunc(3.8)) #3

# y = 2+1j
# print((y)*3)  #(6+3j)

# print(0o20) #16
# print(0xFF) #255
# print(0b1000) #8
# print(oct(64)) #0o100
# print(hex(64)) #0x40
# print(bin(64)) #0b1000000
# print(int('64',8)) #52
# print(int('64',16)) #100
# print(int('1000',2)) #8

# import random
# print(random.random()) #0.876886304959563
# print(random.random()) #0.978604823490934
# print(random.randint(1,10)) #7
# print(random.randint(1,10)) #4

# l1 = ['chai','coffee','coldDrink']
# print(random.choice(l1)) #coldDrink
# print(random.choice(l1)) #chai
# print(random.shuffle(l1))


# print(0.1 +0.1 +0.4) #0.6000000000000001
# print(0.1 +0.1 +0.1) #0.30000000000000004
# print(0.1 +0.1 +0.1 -0.3) #5.551115123125783e-17

# from decimal import Decimal
# print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) #0.3 


# from fractions import Fraction
# myFrac = Fraction (2,7)
# print (myFrac) #2/7

# setOne = {1,2,3,4}
# print(setOne & {1,3}) #{1, 3}
# print(setOne | {1,7}) #{1, 2, 3, 4, 7}
# print(setOne-{1,2,3,4}) #set()
# print(type({})) #<class 'dict'>
# print(type(True)) #<class 'bool'>

# print(True==1) #True
# print(True is 1) #False
# print(True + 4) #5