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

pwdGenFrame = tk.LabelFrame(frame,text="Generate a random password",bd=4)
pwdGenFrame.grid(row = 0,column = 0,sticky="news", padx=20, pady=20)

pwdLengthLabel = tk.Label(pwdGenFrame, text="Length of password: ", font=('Helvetica', 10), anchor="w")
pwdLengthLabel.grid(row = 0,column = 0)
pwdLengthSpin = tk.Spinbox(pwdGenFrame,bd=2, from_=6, to=40, width=5, font=('Helvetica', 10))
pwdLengthSpin.grid(row = 0,column = 1)

for widget in pwdGenFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5, sticky="news")

# minLength = int(input('Enter minimum length: '))
# hasNumber = input('Do you want to have numbers? (y/n): ').lower() == 'y'
# hasSpecial = input('Do you want to have special characters? (y/n): ').lower() == 'y'
# pwd = generatePassword(minLength, hasNumber, hasSpecial)
# print('The generated password is: ',pwd)


window.mainloop()