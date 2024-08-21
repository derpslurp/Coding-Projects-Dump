tile1 = int(input('Choose amount of tile floor: '))
tile2 = int(input('Choose amount of tile floor: '))

product = tile1 * tile2

type = input('Choose material (Porcelain) (Unglazed) (Glazed): ')

if type == 'Porcelain':
    new = product * 53
    print('Your total cost is: $', new)
elif type == 'Unglazed':
    new = product * 27
    print('Your total cost is: $', new)
else:
    new = product * 42
    print('Your total cost is: $', new)
