import random


play_again = 'y'
left = 4
num = str((random.randrange(1000, 10000)))

while play_again == 'y':
    correct = 0
    guess = input('Guess a 4 digit number: ')
    if guess == num:
        print('Correct')
        play_again = input('Play again? (y/n): ').lower()
        left = 4
        num = str((random.randrange(1000, 10000)))

    else:
        for i in range(0,4):
            if guess[i] == num[i]:
                print(num[i],end='')
                correct +=1
                left -= 1
            else:
                print('X',end='')
        print()
        print('Nice, you got',correct,'/ 4')
