from tkinter import *
from tkinter import ttk
from random import *
from json import *

class windows_screen:
    
    def __init__(self, parent):
        self.screen1 = Frame(parent)
        self.screen1.grid(row=0, column=0)
        
        title_bar = Frame(self.screen1)
        title_bar.grid(row=1, column=0)
        title = Label(title_bar, text = "Welcome to Math Quiz",
                                bg = "black", fg = "white", padx = 150, pady = 10,
                                font = ("Time", '14', "bold italic"))
        title.grid(row=0, column=0)
        welcome_info = Label(title_bar, text='Welcome to the mathquiz! This is to test your math potential!', font = ("Calibri", "12"))
        welcome_info.grid(row=1, column=0)
        
        info_bar = Frame(self.screen1)
        info_bar.grid(row=2, column=0, sticky="w")
        ask_name_label = Label(info_bar, text='Enter your full name: ', font = ("Calibri", "12"))
        ask_name_label.grid(row=0, column=0, sticky="W", padx=(12,0))
        self.name_entry = Entry(info_bar, width = 20)
        self.name_entry.grid(row=0, column=1, sticky="W", padx=(12,0))
        ask_age_label = Label(info_bar, text='Enter your age: ', font = ("Calibri", "12"))
        ask_age_label.grid(row=1, column=0, sticky="W", padx=(12,0))
        self.age_entry = Entry(info_bar, width=20)
        self.age_entry.grid(row=1, column=1, sticky="W", padx=(12,0))
        
        diff_bar = Frame(self.screen1)
        diff_bar.grid(row=3, column=0, sticky="W", padx=(12,0))
        diff_info = Label(diff_bar, text="Choose your difficulty below:", font=("Calibri", "12"))
        diff_info.grid(row=0, column=0, sticky="W")
        self.diff_var = StringVar(diff_bar, "1")
        self.difficulties = {'Easy': "0", 
                            'Medium': "1",
                            'Hard': "2"}
        for (option, value) in self.difficulties.items():
            ttk.Radiobutton(diff_bar, text = option, variable = self.diff_var,
                            value = value).grid(row = int(value) + 1, column = 1, pady = 4, sticky ="W")

        start_bar = Frame(self.screen1)
        start_bar.grid(row = 5, column=0, sticky ="W")
        self.error_label = Label(start_bar, fg = "red", font = ("Calibri", "12"))
        self.error_label.grid(row =0, column=0, sticky ="W", padx=(12,0))
        start_button = ttk.Button(start_bar, text = "start quiz", width = 16, command = lambda: self.pre_start_check())
        start_button.grid(row=1, column=0, sticky ="W", padx =(12,0))


    def pre_start_check(self):
        self.errors = []
        self.error_types = {0:"Please enter your name",
                            1:"Please enter your age!",
                            2:"Please enter a number for you age!"}
        #print(self.diff_var.get()) # displays current difficulty
        if len(self.name_entry.get()) < 1:
            self.errors.append(0)
        if len(self.age_entry.get()) < 1:
            self.errors.append(1)
        elif self.age_entry.get().isdigit() == False:
            self.errors.append(2)
        print(f"\n[DEBUG]: {len(self.errors)} errors for user on main screen, error codes:") # ----------------------------------- DEBUG LINE --------------------------------
        print(self.errors)
        if len(self.errors) != 0:
            self.error_label.config(text=(self.error_types[self.errors[0]]))
            self.errors.clear()
        else:
            pass # run math quiz page, back to this part later after making quiz generator









if __name__ == "__main__":
    root = Tk()
    frames = windows_screen(root)
    root.title("MathQuiz")
    root.geometry('500x500')
    root.resizable(False, False)
    root.mainloop() 