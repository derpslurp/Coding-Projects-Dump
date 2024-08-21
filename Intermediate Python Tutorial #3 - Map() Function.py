#Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable
li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

print(list(map(func,li)))