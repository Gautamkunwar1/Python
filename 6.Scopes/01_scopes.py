# username = "hello world"
# def func():
#     username = "Hello"
# print(username) #hello world


# username = "hello world"
# def func():
#     username = "Hello"
#     print(username)
# print(username) #hello world
# func() #Hello


username = "Hello world"
def func():
    print(username)
print(username) #Hello world
func()  #Hello world

# x=99
# def func2(y):
#     z=x+y
#     return z
# result=func2(1)
# print(result) #100

# x=99
# def func3():
#     global x
#     x=12 #not good practice avoid it do not change it 
# func3()
# print(x) #12

# x=99
# def f1():
#     x=88
#     def f2():
#         print(x)
#     f2()
# f1() #88


x=99
def f1():
    x=88
    def f2():
        print(x)
    return f2 #not only reference will go but also all variable and their definition will go 
myResult = f1() 
myResult() #88

def chaicoder(num):
    def actual(x):
        return x** num
    return actual

f = chaicoder(2) #function definition
g = chaicoder(3) #function definition

# print(f) #<function chaicoder.<locals>.actual at 0x0000024BD23DCF40> 
# print(f()) #TypeError: chaicoder.<locals>.actual() missing 1 required positional argument: 'x'

print(f(3)) #9
print(g(3)) #27