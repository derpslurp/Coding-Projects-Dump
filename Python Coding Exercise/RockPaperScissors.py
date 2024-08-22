import random

options = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

done = False

while not done:
    player_pick = input('Pick (Rock/Paper/Scissors): ')
    computer_int = random.randint(0, 2)
    computer_pick = options[computer_int]

    print('You picked {}, Computer picked {}'.format(player_pick, computer_pick))
    if player_pick == 'rock':
        if computer_pick == "Scissors":
            print('You win')
            player_score += 1
            print('You have {} points, Computer has {} points'.format(player_score, computer_score))
        elif computer_pick == "Paper":
            print('You lose')
            computer_score += 1
            print('You have {} points, Computer has {} points'.format(player_score, computer_score))
        elif computer_pick == "Rock":
            print("It's a tie")
            print('You have {} points, Computer has {} points'.format(player_score, computer_score))

    elif player_pick == 'paper':
        if computer_pick == "Scissors":
            print('You lose')
            computer_score += 1
            print('You have {} points, Computer has {} points'.format(player_score, computer_score))
        elif computer_pick == "Rock":
            print('You win')
            player_score += 1
            print('You have {} points, Computer has {} points'.format(player_score, computer_score))
        elif computer_pick == "Paper":
            print("It's a tie")
            print('You have {} points, Computer has {} points'.format(player_score, computer_score))

    elif player_pick == 'scissors':
        if computer_pick == "Paper":
            print('You win')
            player_score += 1
            print('You have {} points, Computer has {} points'.format(player_score, computer_score))
        elif computer_pick == "Rock":
            print('You lose')
            computer_score += 1
            print('You have {} points, Computer has {} points'.format(player_score, computer_score))
        elif computer_pick == "Scissors":
            print("It's a tie")
            print('You have {} points, Computer has {} points'.format(player_score, computer_score))
    else:
        print('Please enter a valid choice')

    if player_score == 10:
        done = True

    if computer_score == 10:
        done = True

if player_score > computer_score:
    print('Final score is {}-{}'.format(player_score, computer_score))
    print('You win!')
else:
    print('Final score is {}-{}'.format(player_score, computer_score))
    print('You lose!')
