import random

def pwdGenerator(noOfPasswords, noOfCharacters):

    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqurstuvwxyz1234567890!@$#%^&*"
    list_ = []
    for i in range(noOfPasswords):
        password = ""
        for j in range(noOfCharacters):
            password = password + random.choice(characters)
        list_.append(password)
    return list_


noOfPasswords = int(input("Enter how many password do you want:"))
noOfCharacters = int(input("Enter how many characters you want in your password:"))
pwd = pwdGenerator(noOfPasswords, noOfCharacters)
print('Your passwords are:')
for each_password in pwd:
    print(each_password)

