import random

words_to_guess = [
    'chime', 'children', 'image', 'film', 'vow', 'kids', 'lungs', 'fake', 'rhyme', 'computer', 'plants', 'take', 'world'
]

def hangman(word):
  display = '_' * len(word)
  guesses = 0
  limit = 5
  letters = list(word)
  guessed = []
  while guesses < limit:
      guess = input(f'Hangman Word: {display} Enter your guess: ')
      while len(guess) == 0 or len(guess) > 1:
          print('Invalid input. Enter a single letter')
          guess = input(
              f'Hangman Word: {display} Enter your guess: ')

      if guess in guessed:
          print('Oops! You already tried that guess, try again!')
          continue

      if guess in letters:
          letters.remove(guess)
          index = word.find(guess)
          display = display[:index] + guess + display[index + 1:]

      else:
          guessed.append(guess)
          guesses += 1
          if guesses == 1:
              print('   _____ \n'
                    '  |      |\n'
                    '  |      |\n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - guesses} guesses remaining\n')

          elif guesses == 2:
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     o\n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - guesses} guesses remaining\n')

          elif guesses == 3:
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     o \n'
                    '  |    /|\ \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - guesses} guesses remaining\n')

          elif guesses == 4:
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     o \n'
                    '  |    /|\ \n'
                    '  |    / \n'
                    '  |      \n'
                    '__|__\n')
              print(f'Wrong guess: {limit - guesses} guesses remaining\n')

          elif guesses == 5:
              print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     o \n'
                    '  |    /|\ \n'
                    '  |    / \ \n'
                    '  |     \n'
                    '__|__\n')
              print("Wrong guess, you've been hanged!")
              print(f'The word was: {word}')

      if display == word:
          print(f'Congrats! You have guessed the word {word} correctly!')
          break


def play_hangman():
   play = input('Would you like to play hangman?(y/n): ')
   play2 = False
   while play.lower() == 'y' or play2:
       word = random.choice(words_to_guess)
       hangman(word)
       play2 = play_again()
       play = 'n'

   exit()

def play_again():
  play = input('Would you like to play again?(y/n): ')

  if play.lower() == 'y':
      return True
  elif play.lower() == 'n':
      return False

play_hangman()