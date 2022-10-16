from logging import root
from tkinter import *
root = Tk()
MyLabel1 = Label(root, text="Hello Python World!")
MyLabel2 = Label(root, text="My Name Is Rajkumar Rajbhar")
MyLabel1.grid(row=0, column=0)
MyLabel2.grid(row=1,column=5)
root.mainloop()