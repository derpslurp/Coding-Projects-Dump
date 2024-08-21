import random

player_score = 0
computer_score = 0

while True:
    choices = ['rock','paper','scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper, scissors?: ').lower()

    if player == computer:
        print('computer: ',computer)
        print('player: ',player)
        print('Tie')
        print('Score: ',player_score,'-',computer_score)
    elif player == 'rock':
        if computer == 'paper':
            print('computer: ', computer)
            print('player: ', player)
            print('You lose')
            computer_score +=1
            print('Score: ', player_score, '-', computer_score)
        if computer == 'scissors':
            print('computer: ', computer)
            print('player: ', player)
            print('You win')
            player_score +=1
            print('Score: ', player_score, '-', computer_score)
    elif player == 'paper':
        if computer == 'scissors':
            print('computer: ', computer)
            print('player: ', player)
            print('You lose')
            computer_score += 1
            print('Score: ', player_score, '-', computer_score)
        if computer == 'rock':
            print('computer: ', computer)
            print('player: ', player)
            print('You win')
            player_score += 1
            print('Score: ', player_score, '-', computer_score)
    elif player == 'scissors':
        if computer == 'rock':
            print('computer: ', computer)
            print('player: ', player)
            print('You lose')
            computer_score += 1
            print('Score: ', player_score, '-', computer_score)
        if computer == 'paper':
            print('computer: ', computer)
            print('player: ', player)
            print('You win')
            player_score += 1
            print('Score: ', player_score, '-', computer_score)
    play_again = input('Play again? (y/n): ').lower()
    if play_again != 'y':
        break
print('stupid ah monke')