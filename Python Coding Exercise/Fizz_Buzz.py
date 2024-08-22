def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizz Buzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

user_input = int(input('Enter a number: '))
print(fizz_buzz(user_input))