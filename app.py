import string
import random
import tkinter as tk
from tkinter import Button


def generatePassword():
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    pwdLength = int(pwdLengthSpin.get())
    numbers = includeNumbers.get()
    specialChars = includeSpecialChars.get()

    char = letters
    if numbers:
        char += digits
    if specialChars:
        char += special

    pwd = ''
    meetsCriteria = False
    hasNumber = False
    hasSpecial = False

    while not meetsCriteria or len(pwd) < pwdLength:
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
    print(pwd)
    return pwd

# def printStuff():
#     print('The length of the password is: ', pwdLengthSpin.get())
#     print('The number box is set to: ', includeNumbers.get())
#     print('The special box is set to: ', includeSpecialChars.get())   
          
# Create the main window
window = tk.Tk()
window.title('Password Generator')
window.geometry('400x400')

# define variables
pwdLength = 0
includeNumbers =  tk.BooleanVar() 
includeSpecialChars =  tk.BooleanVar()

# Create the first frame inside the main window
frame = tk.Frame(window)
frame.pack()

inputFrame = tk.LabelFrame(frame,text="Generate a random password",bd=4)
inputFrame.grid(row = 0,column = 0,sticky="news", padx=20, pady=20)

pwdLengthLabel = tk.Label(inputFrame, text="Length of password: ", font=('Helvetica', 10), anchor="w")
pwdLengthLabel.grid(row = 0,column = 0)
pwdLengthSpin = tk.Spinbox(inputFrame,bd=2, from_=8, to=40, width=5, font=('Helvetica', 10))
pwdLengthSpin.grid(row = 0,column = 1)

includeNumberLabel = tk.Label(inputFrame, text="Include Numbers: ", font=('Helvetica', 10), anchor="w")
includeNumberLabel.grid(row = 1,column = 0)
includeNumberCheck = tk.Checkbutton(inputFrame, text="", onvalue=True, offvalue=False, variable=includeNumbers, font=('Helvetica', 10))
includeNumberCheck.grid(row = 1,column = 1)

includeSpecialLabel = tk.Label(inputFrame, text="Include Special Characters: ", font=('Helvetica', 10), anchor="w")
includeSpecialLabel.grid(row = 3,column = 0)
includeSpecialCheck = tk.Checkbutton(inputFrame, text="", onvalue=True, offvalue=False, variable=includeSpecialChars, font=('Helvetica', 10))
includeSpecialCheck.grid(row = 3,column = 1)

# create output frame
buttonFrame = tk.LabelFrame(frame,bd='0')
buttonFrame.grid(row=2,column=0,padx=10,pady=10)

# create the button frame
buttonFrame = tk.LabelFrame(frame,bd='0')
buttonFrame.grid(row=2,column=0,padx=10,pady=10)
genPwdButton = Button(buttonFrame,text='Generate Password',bd='4',font=('Helvetica',10), command=generatePassword)
genPwdButton.grid(row=0,column=0,ipadx=5,ipady=5,padx=10,pady=10)

for widget in inputFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5, sticky="news")

# pwdLength = int(input('Enter pwd length: '))
# hasNumber = input('Do you want to have numbers? (y/n): ').lower() == 'y'
# hasSpecial = input('Do you want to have special characters? (y/n): ').lower() == 'y'
# pwd = generatePassword(pwdLength, hasNumber, hasSpecial)
# print('The generated password is: ',pwd)


window.mainloop()