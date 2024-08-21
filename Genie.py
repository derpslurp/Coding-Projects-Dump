number = input('Think of a number between 1-10, is your number even y/n: ')
even_numbers = []
odd_numbers = []
if number == 'y':
    for number in range(1, 10):
        if number % 2 == 0:
            even_numbers.append(number)
    number2 = input('If you spelled your number out, does it have 3 letters y/n: ')
    if number2 == 'y':
        number3 = input('Is your number greater or less than 3 g/l: ')
        if number3 == 'g':
            number4 = input('Is your number greater or less than 8 g/l: ')
            if number4 == 'g':
                print('Your number is 10')
            else:
                print('Your number is 6')
        else:
            print('Your number is 2')
    else:
        number5 = input('Is your number greater or less than 6 g/l: ')
        if number5 == 'g':
            print('your number is 8')
        else:
            print('your number is 4')
else:
    for number in range(1, 10):
        if number % 2 == 1:
            odd_numbers.append(number)
    number2 = input('If you spelled your number out, does it have 4 letters y/n: ')
    if number2 == 'y':
        number3 = input('Is your number greater or less than 7 g/l: ')
        if number3 == 'g':
            print('Your number is 9')
        else:
            print('Your number is 5')
    else:
        number5 = input('If you spelled your number out, does it have 5 letters y/n: ')
        if number5 == 'y':
            number6 = input('is your number greater or less than 5 g/l: ')
            if number6 == 'g':
                print('Your number is 7')
            else:
                print('your number is 3')
        else:
            print('your number is 1')
