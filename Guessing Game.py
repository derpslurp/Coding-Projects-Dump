secret_word = "chingchong"
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input('Enter guess: ')
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Lmao what a loser u lost, bro can't even guess the word in 3 tries lmaoooo")
else:
    print('You win!')