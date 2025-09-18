#Generator function with yield 
#Write a generator function that yields even numbers up to a specified limit.

#General Method
def even_generator(limit):
    li =[]
    for i in range(2,limit+1,2):
        li.append(i)
    return li #return a list but we don't want
    
print(even_generator(10)) #[2, 4, 6, 8, 10]

#or
def even_generator(limit):
    for i in range(2,limit+1,2):
        return i 
    
print(even_generator(10)) #output => 2 only

#or
# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         return i 

# for num in even_generator(10):
#     print(num) #    for num in even_generator(10):
#                ~~~~~~~~~~~~~~^^^^
# TypeError: 'int' object is not iterable

# yield
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i 

for num in even_generator(10):
    print(num)
    
# 2
# 4
# 6
# 8
# 10