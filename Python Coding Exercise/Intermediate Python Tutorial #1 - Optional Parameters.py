#Sets a default value to a parameter in case of error
def func(word, add=5, freq=1):
    print(word * (freq+add))

call = func('tim')