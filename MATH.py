database = {'Beanie': '123456'}
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")
pw_tries = 0
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = input("Incorrect password. Try again: ")
            pw_tries += 1
            if pw_tries == 3:
                print('Too many attempts')
                break
        break
if pw_tries < 3:
    print('Verified')
else:
    print('Suspicious activity')
