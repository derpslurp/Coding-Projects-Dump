
user_input = int(input('How many Fibonacci Sequences do you want?: '))

num1 = 1

num2 = 1

num3 = 102038138123

for i in range(0, user_input):
    num3 = num1 + num2

    num1 = num2
    num2 = num3

print(num3)