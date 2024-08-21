def mygenerator():
    yield 3
    yield 2
    yield 3

g = mygenerator()

print(sum(g))
#generators are a function that returns an iterator that produces a sequence of values when iterated over