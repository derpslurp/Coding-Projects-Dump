def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + 'GOOGOOGAAGAA'
            else:
                translation = translation + 'googoogaagaa'
        else:
            translation = translation + letter
    return translation


print(translate(input('Enter a word to convert to baby language: ')))
