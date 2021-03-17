from tkinter import *
from tkinter import ttk
from random import *
from json import dump, load
import os
from time import gmtime, strftime

FILES_FOLDER = "./mathquiz_files/"
QUIZ_CONFIG = "quiz_config.json"

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
        
        # Insert smart_brain method here that grabs the question configs

        for (option, value) in smart_brain.difficulties_choice.items():
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
        if len(self.name_entry.get()) < 1:
            self.errors.append(0)
        if len(self.age_entry.get()) < 1:
            self.errors.append(1)
        elif self.age_entry.get().isdigit() == False:
            self.errors.append(2)
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - {len(self.errors)} errors for user on main screen, error codes: {str(self.errors)}")
        if len(self.errors) != 0:
            self.error_label.config(text=(self.error_types[self.errors[0]]))
            self.errors.clear()
        else:
            pass # run math quiz page, back to this part later after making quiz generator



class background_tasks:
    def __init__(self):
        with open((FILES_FOLDER + QUIZ_CONFIG), "r") as read_config:
            self.config_data = load(read_config)
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - length of quiz config: {len(self.config_data)}")
        # Close file
        self.difficulties_choice = {}
        for i in range(len(self.config_data)):
            self.difficulties_choice.update({(self.config_data[str(i)]["name"]):str(i)})


if __name__ == "__main__":
    # Process below basically checks if the required files are in the directory set above in the program
    # The program will create the files and directories if they do not exist
    print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - locating '{FILES_FOLDER + QUIZ_CONFIG}'")
    if os.path.isfile(FILES_FOLDER + QUIZ_CONFIG) != True:
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - cannot find file, changing working directory!")
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - current working directory changed to current python file location")
    print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - current working directory: '{os.getcwd()}'")
    if os.path.isfile(FILES_FOLDER + QUIZ_CONFIG) == True:
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - status of '{FILES_FOLDER + QUIZ_CONFIG}': online")
        pass
    else:
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - '{FILES_FOLDER + QUIZ_CONFIG}' is offline, creating file")
        if os.path.isdir(FILES_FOLDER) != True:
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - '{FILES_FOLDER}' directory cannot be found, creating directory")
            os.mkdir(FILES_FOLDER)
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - created directory: '{FILES_FOLDER}' directory")
        else:
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - '{FILES_FOLDER}' folder exists")
            pass
        # This is the default config for the mathquiz, I made it so people can change the config themeselves and have their own difficulties for more dynamic use
        default_math_quiz_config = {
            "0":{
                "name": "Easy",
                "number_range":  ["0", "10"],
                "operators": ["+", "-"],
                "question_length": 2
                },
            "1":{
                "name": "Medium",
                "number_range":  ["0", "15"],
                "operators": ["+", "-", "*"],
                "question_length": 3
                },
            "2":{
                "name": "Hard",
                "number_range":  ["0", "20"],
                "operators": ["+", "-", "*", "/"],
                "question_length": 4
                }
            }
        with open((FILES_FOLDER + QUIZ_CONFIG), 'a+') as json_f:
            dump(default_math_quiz_config, json_f, indent=4)
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] - '{FILES_FOLDER + QUIZ_CONFIG}' file created and is online!")
    
    root = Tk()
    smart_brain = background_tasks()
    main_screen = windows_screen(root)
    root.title("MathQuiz")
    #root.geometry('500x300')
    root.resizable(False, False)
    root.mainloop()