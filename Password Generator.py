import random

password = list()
numbers = list('0123456789')
special_characters = list('!@#$%^&*()')
letters_lower = list('abcdefghijklmnpoqrstuvwxyz')
letters_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

a = random.sample(numbers, 3)
a2 = ''.join(a)
b = random.sample(special_characters, 4)
b2 = ''.join(b)
c = random.sample(letters_lower, 6)
c2 = ''.join(c)
d = random.sample(letters_upper, 4)
d2 = ''.join(d)

password.append(a2)
password.append(b2)
password.append(c2)
password.append(d2)

password_mid = ''.join(password)
password_final = random.sample(password_mid, 17)
password_final2 = ''.join(password_final)
print(password_final2)
