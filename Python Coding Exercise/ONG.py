from textblob import TextBlob

words = []
user_input = input('Type a word and phase with a typo: ')

words.append(user_input)
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words:", ''.join(words))
print("Corrected Words are: ")
for i in corrected_words:
    print(i.correct(), end=" ")