import string
import random
import tkinter as tk



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

# Create the main window
window = tk.Tk()
window.title('Password Generator')
window.geometry('400x400')

# Create the first frame inside the main window
frame = tk.Frame(window)
frame.pack()

# pwdGen = tk.LabelFrame(frame,text="Password Generator",bd=4)
# pwdGen.grid(row = 0,column = 0,sticky="news", padx=20, pady=20)

# minLength = int(input('Enter minimum length: '))
# hasNumber = input('Do you want to have numbers? (y/n): ').lower() == 'y'
# hasSpecial = input('Do you want to have special characters? (y/n): ').lower() == 'y'
# pwd = generatePassword(minLength, hasNumber, hasSpecial)
# print('The generated password is: ',pwd)


window.mainloop()