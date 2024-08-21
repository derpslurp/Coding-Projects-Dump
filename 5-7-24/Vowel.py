user_input = input('Enter a phrase: ')

vowels = 0
for i in user_input:
    if i == 'a':
        vowels += 1
    elif i == 'e':
        vowels += 1
    elif i == 'i':
        vowels += 1
    elif i == 'o':
        vowels += 1
    elif i == 'u':
        vowels += 1
print('There are', vowels, 'vowels in this sentence')