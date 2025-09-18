# >>> D = {'a':1,'b':2}
# >>> for key in D.keys():
# ...     print(key)
# ... 
# a
# b

# next(I) == __next__()

# >>> I = iter(D)
# >>> I
# <dict_keyiterator object at 0x0000027D6E4B8F40>

# >>> next(I)
# 'a'
# >>> next(I)
# 'b'
# >>> next(I)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^
# StopIteration