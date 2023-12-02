import string
import random

def generatePassword(minLength, numbers=True, specialChars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    # print(letters, digits, special)
    
    char = letters
    if numbers:
        char += digits
    if specialChars:
        char += special

    pwd = ''
    meetsCriteria = False
    hasNumber = False
    hasSpecial = False

    while not meetsCriteria or len(pwd) < minLength:
        newChar = random.choice(char)
        pwd += newChar

        if newChar in digits:
            hasNumber = True
        elif newChar in special:
            hasSpecial = True

        meetsCriteria = True
        if numbers:
            meetsCriteria = hasNumber
        if specialChars:
            meetsCriteria = meetsCriteria and hasSpecial
    return pwd

minLength = int(input('Enter minimum length: '))
hasNumber = input('Do you want to have numbers? (y/n): ').lower() == 'y'
hasSpecial = input('Do you want to have special characters? (y/n): ').lower() == 'y'
pwd = generatePassword(minLength, hasNumber, hasSpecial)
print('The generated password is: ',pwd)