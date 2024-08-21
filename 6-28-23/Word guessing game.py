import random

words = ['chicken','sushi','crate','plant','house','board','lamp','zoo','cow']

guesses = ''
turns = 12

word = random.choice(words)

while turns > 0:
    words_left = 0
    for char in word:
        if char in guesses:
            print(char,end='')
        else:
            print("_",end='')
            words_left += 1
    if words_left == 0:
        print()
        print("You win")
        print("The word was:", word)
        break
    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("stupid u lost")