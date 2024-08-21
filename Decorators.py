def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)
#decorators can allow a user to add new functionality to an existing object without modifying its structure