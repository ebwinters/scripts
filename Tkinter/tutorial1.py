import sys
from tkinter import *

mGui = Tk()
mGui.geometry('450x450+200+200')
mGui.title('My Tkinter Interface')
# mLabel = Label(text='My Label', fg='red', bg='blue')
# mLabel.place(x=100, y=225)



mLabel2 = Label(text='My Second Label', fg='red', bg='blue')
mLabel2.grid(row=0, column=0)

mLabel3 = Label(text='My Third Label', fg='red', bg='blue')
mLabel3.grid(row=1, column=0, sticky=E)

mLabel4 = Label(text='My Fourth Label', fg='red', bg='blue')
mLabel4.grid(row=0, column=1, sticky=W)


mGui.mainloop()

