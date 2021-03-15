from tkinter import *
from tkinter import ttk
from random import *
from json import *

class windows_screen:
    
    def __init__(self, parent):
        self.title_bar = Frame(parent)
        self.title_bar.grid(row=1, column=0)
        title = Label(self.title_bar, text = "Welcome to Math Quiz",
                                bg = "black", fg = "white", padx = 150, pady = 10,
                                font = ("Time", '14', "bold italic"))
        title.grid(row=0, column=0)
        welcome_info = Label(self.title_bar, text='Welcome to the mathquiz! This is to test your math potential!', font = ("Calibri", "12"))
        welcome_info.grid(row=1, column=0)

if __name__ == "__main__":
    root = Tk()
    frames = windows_screen(root)
    root.title("MathQuiz")
    root.geometry('500x500')
    root.resizable(False, False)
    root.mainloop()