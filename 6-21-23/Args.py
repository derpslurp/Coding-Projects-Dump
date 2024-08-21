def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,1,1,3,6,1,10))