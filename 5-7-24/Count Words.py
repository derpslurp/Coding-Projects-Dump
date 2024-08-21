user_input = input('Enter a phrase: ')

words = 1
for i in user_input:
    if i == ' ':
        words += 1
print('There is', words, 'words in this sentence')