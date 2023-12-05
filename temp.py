import string
import random

def genPass(length, hasNum, hasSpec):
    lettersLower = string.ascii_lowercase
    lettersUpper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    chars = lettersLower + lettersUpper
    if hasNum == True:
        chars += digits
    if hasSpec == True:
        chars += special
    # print(chars)
    
    pw = []
    pw.append(random.choice(lettersLower))
    pw.append(random.choice(lettersUpper))
    pw.append(random.choice(digits))
    pw.append(random.choice(special))

    for i in range(length - 4):
        pw.append(random.choice(chars))
    random.shuffle(pw)
    pw = "".join(pw)
    print(pw)
         
    



genPass(10, True, False)
