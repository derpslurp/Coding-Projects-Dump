num1 = int(input('Enter a number: '))
num2 = int(input('Enter a power for that number: '))


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(num1, num2))