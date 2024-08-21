def whole_number(number):
    return number == int(number)

while True:
    final = []
    user_input = int(input("Type in a number to find it's factors: "))
    for i in range(1, user_input+1):
        factor = user_input / i
        yn = whole_number(factor)
        if yn == False:
           pass
        else:
            yuh = int(factor)
            final.append(yuh)
    print(final)

    if int(len(final)) <= 2:
        print('This number is a prime number')



