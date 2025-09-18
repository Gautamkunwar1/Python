#function with *args
#write a function that takes variable number of arguments and return their sum

# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2)) #3
# print(sum_all(1,2,3))   #6
# print(sum_all(1,2,3,4,5))   #15


#we can use any name in parameter but use of * is mandatory 
# def sum_all(*chai): 
#     return sum(chai)

# print(sum_all(1,2)) #3
# print(sum_all(1,2,3))   #6
# print(sum_all(1,2,3,4,5))   #15

def sum_all(*args):
    print(*args)
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))

#Output
# 1 2
# 3
# 1 2 3
# 6
# 1 2 3 4 5
# 15

def sum_all(*args):
    print(args)
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))

#Output => gives in tuple
# (1, 2)
# 3
# (1, 2, 3)
# 6
# (1, 2, 3, 4, 5)
# 15


def sum_all(*args):
    for i in args:
        print(i*2) #yes it is multiplying value
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3))