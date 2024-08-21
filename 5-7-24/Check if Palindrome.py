user_input = input('Type in a word to see if it is the same spelled backwards: ')

word = user_input
def flip(x):
  return x[::-1]

new_word = flip(user_input)

print(user_input)
print(new_word)

if word == new_word:
    print('This word is palindrome')