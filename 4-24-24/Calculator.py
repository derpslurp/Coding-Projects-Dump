while True:
    user1 = str(input('Type first number: '))
    user2 = str(input('Type second number: '))
    user3 = str(input('Type mathmatical symbol: '))

    list = [user1, user3, user2]

    p = ''.join(list)

    print(list, '=', int(eval(p)))
