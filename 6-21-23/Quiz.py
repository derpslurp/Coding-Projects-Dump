def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('---------------------------')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input('Enter (A or B): ')
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print('CORRECT')
        return 1
    else:
        print('WRONG STUPID')
        return 0

def display_score(correct_guesses,guesses):
    print('----------------------')
    print('RESULTS')
    print('----------------------')

    print('Answers: ',end=' ')
    for i in questions:
        print(questions.get(i),end=' ')
    print()

    print('Guesses: ',end=' ')
    for i in guesses:
        print(i,end=' ')
    print()

    score = int((correct_guesses/len(questions))*100)
    print('Your score is: '+str(score)+'%')
    if score < 100:
        print('stupid monke')

def play_again():
    response = input('Play again? (y/n): ')
    response = response.upper()

    if response == 'Y':
        return True
    else:
        return False

questions = {
    'You like men?: ': 'A',
    'You gay?: ': 'A',
    'You dumb?: ': 'A',
}

options = [['A. yes', 'B. no'],
           ['A. yes', 'B. no'],
           ['A. yes', 'B. no']]

new_game()
while play_again():
    new_game()

print('ur ugly')