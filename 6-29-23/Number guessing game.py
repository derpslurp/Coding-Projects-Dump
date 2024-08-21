import random

number_range = []
tries_left = 5
play_again = 'y'

while play_again == 'y':
    number_range = []
    tries_left = 5
    first_num = int(input('Type a number: '))
    second_num = int(input('Type a number larger than your first number: '))
    for i in range(first_num,second_num):
        number_range.append(i)

    mys_num = random.choice(number_range)
    guess_in = 0

    while tries_left > 0:
        guess = int(input('Guess the number inbetween the 2 numbers you picked: '))
        if guess == mys_num:
            print('You win')
            guess_in +=1
            print('You guessed it in',str(guess_in),'tries')
            break
        else:
            print('Wrong')
            tries_left -=1
            guess_in += 1
    if tries_left <= 0:
        print('You failed to guess the number')
        print('The number was: ',str(mys_num))
        play_again = input('Play again? (y/n): ').lower()
    play_again = input('Play again? (y/n): ').lower()
    if play_again != 'y':
        print('grrrr')
        break


