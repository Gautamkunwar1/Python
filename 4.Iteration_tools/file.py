import time

print("Chai is here")

username = "Python"
print(username)

# >>> f = open('first.py')
# >>> iter(f) is f
# True

# >>> iter(f) is f.__iter__()
# True

#Read from file in integrated terminal
# file ka khud ka iter tool hota hai

# >>> f=open ('first.py')
# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'print("Chai is here")\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'username = "Python"\n'
# >>> f.readline()
# 'print(username)'
# >>> f.readline()
# ''

#Raw method
# >>> f = open('first.py')
# >>> f.__next__()
# 'import time\n'
# >>> f.__next__()        
# '\n'
# >>> f.__next__()
# 'print("Chai is here")\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# 'username = "Python"\n'
# >>> f.__next__()
# 'print(username)\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^^
# StopIteration
# >>>


#loop method

# >>> for line in open('first.py'):
# ...     print(line)
#output
# ... 
# import time



# print("Chai is here")



# username = "Python"

# print(username)


#via While Loop
# >>> f = open('first.py')
# >>> while True:
# ...     line = f.readline()
# ...     if not line: break
# ...     print(line,end='')

#Output
# import time

# print("Chai is here")

# username = "Python"
# print(username)