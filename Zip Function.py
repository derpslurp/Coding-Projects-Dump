usernames = ["Dude", "Bro", "Mister"]
passwords = ('p@ssword', "abc123", 'guest')

users = dict(zip(usernames,passwords))
print(type(users))

for key,value in users.items():
    print(key+' : '+value)