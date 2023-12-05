import string
import random
import tkinter as tk
from tkinter import Button
import pyperclip as pc


def genPass(length, hasNum, hasSpec):
    chars = []
    lettersLower = string.ascii_lowercase
    lettersUpper = string.ascii_uppercase
    digits = string.digits
    special = "".join(['!', '#', '$', '%', '&', '(', ')', '*', '+'])
    chars = lettersLower + lettersUpper
    if hasNum == True:
        chars += digits
    if hasSpec == True:
        chars += special
    pw = []
    pw.append(random.choice(lettersLower))
    pw.append(random.choice(lettersUpper))
    pw.append(random.choice(digits))
    pw.append(random.choice(special))

    for i in range(int(length) - 4):
        pw.append(random.choice(chars))
    random.shuffle(pw)
    pw = "".join(pw)
    outputFrame = tk.LabelFrame(frame,text="",bd=0)
    outputFrame.grid(row = 1,column = 0,sticky="news", padx=20, pady=20)
    outputLabel = tk.Label(outputFrame, text=f'You password is = {pw}', font=('Helvetica', 10), padx=20)
    outputLabel.grid(row = 0,column = 0)
    genPwdButton.grid_remove()
    copyButton = Button(buttonFrame,text='Copy Password',bd='4',font=('Helvetica',10), command=lambda: (copyPass(pw)))
    copyButton.grid(row=0,column=0,ipadx=5,ipady=5,padx=10,pady=10)
    closeButton = Button(buttonFrame,text='Close',bd='4',font=('Helvetica',10), command=window.destroy)
    closeButton.grid(row=1,column=0,ipadx=5,ipady=5,padx=10,pady=10)

def copyPass(password):     #copy text to clipboard
    pc.copy(password)

# Create the main window
window = tk.Tk()
window.title('Password Generator')
# window.geometry('400x400')

# define variables
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
# outputFrame = tk.LabelFrame(frame,text="",bd=0)
# outputFrame.grid(row = 1,column = 0,sticky="news", padx=20, pady=20)
# outputLabel = tk.Label(outputFrame, text=f'You password is = {pw}', font=('Helvetica', 10), padx=20)
# outputLabel.grid(row = 0,column = 0)

# create the button frame
buttonFrame = tk.LabelFrame(frame,borderwidth = 1, bd='0')
buttonFrame.grid(row=2,column=0,padx=10,pady=10)
genPwdButton = Button(buttonFrame,text='Generate Password',bd='4',font=('Helvetica',10), command=lambda: genPass(pwdLengthSpin.get(), includeNumbers.get(), includeSpecialChars.get() ))
genPwdButton.grid(row=0,column=0,ipadx=5,ipady=5,padx=10,pady=10)

for widget in inputFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5, sticky="news")

# pwdLength = int(input('Enter pwd length: '))
# hasNumber = input('Do you want to have numbers? (y/n): ').lower() == 'y'
# hasSpecial = input('Do you want to have special characters? (y/n): ').lower() == 'y'
# pwd = generatePassword(pwdLength, hasNumber, hasSpecial)
# print('The generated password is: ',pwd)


window.mainloop()