#Allows you to filter out items based on the condition
def add7(x):
    return x+7
def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]
b = list(filter(isOdd,a))
print(b)