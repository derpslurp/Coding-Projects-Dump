fib_cache = {}


def fib_memo(input_val):
    if input_val in fib_cache:
        return fib_cache[input_val]

    if input_val == 0:
       val = 0
    elif input_val < 2:
       val = 1
    else:
       val = fib_memo(input_val - 1) + fib_memo(input_val - 2)

    fib_cache[input_val] = val
    return val


if __name__ == '__main__':
    user_input = int(input('Enter how many numbers you want to generate: '))
    for i in range(user_input):
        print(f'Fibonacci ({i}) : {fib_memo(i)}')