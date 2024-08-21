import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operations = ['+', '-', '*', '/']
answer = []

play = input('Would you like to play a math game?(y/n): ')

while play.lower() == 'y':
    answer = []
    final_answer = ''
    roll1 = random.randint(0, 9)
    roll2 = random.randint(0, 3)
    roll3 = random.randint(0, 9)

    number1 = numbers[roll1]
    answer.append(number1)

    operator = operations[roll2]
    answer.append(operator)

    number2 = numbers[roll3]
    answer.append(number2)

    final_answer = ''.join(answer)
    real_answer = eval(final_answer)
    real_answer2 = int(real_answer)

    player_answer = input('What is {}(no fractions): '.format(final_answer))
    player_answer2 = int(float(player_answer))
    if player_answer2 == real_answer2:
        print('Congrats, that is correct')
    else:
        print("That's incorrect, the correct answer is {}".format(real_answer))
    play = input('Would you like to play again?(y/n): ')
