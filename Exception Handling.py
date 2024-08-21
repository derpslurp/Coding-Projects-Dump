try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("You can't divide by 0 idiot")
except ValueError:
    print('Enter only numbers stupid')
except Exception:
    print('Something went wrong')