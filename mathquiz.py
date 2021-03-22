from tkinter import *
from tkinter import ttk
from random import randint, choice
from json import dump, load
import os
from time import localtime, strftime

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

        self.diff_var.set(0)
        start_bar = Frame(self.screen1)
        start_bar.grid(row = 5, column=0, sticky ="W")
        self.error_label = Label(start_bar, fg = "red", font = ("Calibri", "12"))
        self.error_label.grid(row =0, column=0, sticky ="W", padx=(12,0))
        start_button = ttk.Button(start_bar, text = "start quiz", width = 16, command = lambda: self.pre_start_check(parent))
        start_button.grid(row=1, column=0, sticky ="W", padx =(12,0), pady=(0,12))


    def post_start_check(self, parent):
        self.screen1.grid_remove()
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - Screen 1 removed, starting screen 2")
        self.math_data = smart_brain.generate_quiz(smart_brain.config_data[str(self.diff_var.get())])
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - self.math_data variable: {self.math_data}")
        self.score = {}
        self.screen2 = Frame(parent)
        self.screen2.grid(sticky="W")
        
        title_bar = Frame(self.screen2)
        title_bar.grid(sticky="W")
        self.question_title = Label(title_bar, text = f"Quiz Number: 1/{str(len(self.math_data))}",
                                bg = "black", fg = "white", padx = 150, pady = 10,
                                font = ("Time", '14', "bold italic"))
        self.question_title.grid(sticky="W", row = 0)
        self.current_question_number = 1
        question_bar = Frame(self.screen2)
        question_bar.grid(sticky="W", row = 1)
        self.question_quiz = Label(question_bar, text=f"{''.join(self.math_data[self.current_question_number][0])} = ", font = ("Calibri", "12"))
        self.question_quiz.grid(sticky="W", row =0, column =0, padx=(12,0))
        answer_entry = Entry(question_bar, width=12)
        answer_entry.grid(sticky="W", row =0, column=1)
        submit_button = ttk.Button(text="Submit", width = 12, command = lambda: self.submit_answer(answer_entry.get()))
        submit_button.grid(sticky="w", row =1, column = 0)



    def submit_answer(self, answer):
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - User attempted to submit answer [{answer}], while correct answer should be [{self.math_data[self.current_question_number][1]}]")
        if int(answer) == int(self.math_data[self.current_question_number][1]):
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - User answer correct!")
        else:
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - User answer incorrect!")

    def pre_start_check(self, parent):
        self.errors = []
        if len(self.name_entry.get()) < 1:
            self.errors.append(0)
        if len(self.age_entry.get()) < 1:
            self.errors.append(1)
        elif self.age_entry.get().isdigit() == False:
            self.errors.append(2)
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - {len(self.errors)} errors for user on main screen, error codes: {str(self.errors)}")
        if len(self.errors) != 0:
            self.error_types = {0:"Please enter your name",
                            1:"Please enter your age!",
                            2:"Please enter a number for you age!"}
            self.error_label.config(text=(self.error_types[self.errors[0]]))
            self.errors.clear()
        else:
            self.post_start_check(parent)
            pass # run math quiz page



class background_tasks:
    def __init__(self):
        with open((FILES_FOLDER + QUIZ_CONFIG), "r") as read_config:
            self.config_data = load(read_config)
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - length of quiz config: {len(self.config_data)}")
        # Close file
        self.difficulties_choice = {}
        for i in range(len(self.config_data)):
            self.difficulties_choice.update({(self.config_data[str(i)]["name"]):str(i)})
            
    def generate_quiz(self, level_data):
        try:
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - chosen data: {level_data}")
            data_output = {}
            operators = ['+', '-', '/', '*']
            for number in range(level_data["number_of_questions"]):
                number += 1
                current_question = []
                for q_length in range(level_data["question_length"]):
                    current_question.append(str(randint(level_data["number_range"][0], level_data["number_range"][1])))
                    current_question.append(f' {choice(level_data["operators"])} ')
                
                current_question.pop()
                current_question_string = ''.join(current_question)
                print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - Displaying questions: {current_question_string}")
                if '/ 0' in current_question_string:
                    print('encountered divide by zero')
                    current_question_string = current_question_string.replace("/ 0", f'/ {(randint((level_data["number_range"][0] + 1), level_data["number_range"][1]))}')
                    print(current_question_string)
                print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - Question [{number}/{level_data['number_of_questions']}] {current_question_string + ' = ' + str(round(eval(current_question_string), 2))}")
                data_output.update({number:[current_question_string, round(eval(current_question_string), 2)]})
                print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - Added question  [{number}/{level_data['number_of_questions']}] to questions database")
            
            # DEBUG PURPOSES:
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - Listing questions and answers in database:")
            
            for i in data_output.keys():
                print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - {data_output[i]}")
                pass

            return data_output
        except:
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - Corrupted quiz_config.json file, unable to generate quiz, remove quiz_config.json and restart the program!")
            return 0


if __name__ == "__main__":
    # Process below basically checks if the required files are in the directory set above in the program
    # The program will create the files and directories if they do not exist
    print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - locating '{FILES_FOLDER + QUIZ_CONFIG}'")
    if os.path.isfile(FILES_FOLDER + QUIZ_CONFIG) != True:
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - cannot find file, changing working directory!")
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - current working directory changed to current python file location")
    print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - current working directory: '{os.getcwd()}'")
    if os.path.isfile(FILES_FOLDER + QUIZ_CONFIG) == True:
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - status of '{FILES_FOLDER + QUIZ_CONFIG}': online")
        pass
    else:
        print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - '{FILES_FOLDER + QUIZ_CONFIG}' is offline, creating file")
        if os.path.isdir(FILES_FOLDER) != True:
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - '{FILES_FOLDER}' directory cannot be found, creating directory")
            os.mkdir(FILES_FOLDER)
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - created directory: '{FILES_FOLDER}' directory")
        else:
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - '{FILES_FOLDER}' folder exists")
            pass
        # This is the default config for the mathquiz, I made it so people can change the config themeselves and have their own difficulties for more dynamic use
        default_math_quiz_config = {
            "0":{
                "name": "Easy",
                "number_range":  [0, 10],
                "operators": ["+", "-"],
                "question_length": 2,
                "number_of_questions": 5
                },
            "1":{
                "name": "Medium",
                "number_range":  [0, 15],
                "operators": ["+", "-", "*"],
                "question_length": 3,
                "number_of_questions": 10
                },
            "2":{
                "name": "Hard",
                "number_range":  [0, 20],
                "operators": ["+", "-", "*", "/"],
                "question_length": 4,
                "number_of_questions": 15
                }
            }
        with open((FILES_FOLDER + QUIZ_CONFIG), 'a+') as json_f:
            dump(default_math_quiz_config, json_f, indent=4)
            print(f"[DEBUG] [{strftime('%Y-%m-%d %H:%M:%S', localtime())}] - '{FILES_FOLDER + QUIZ_CONFIG}' file created and is online!")
    
    root = Tk()
    smart_brain = background_tasks()
    main_screen = windows_screen(root)
    root.title("MathQuiz")
    #root.geometry('500x300')
    root.resizable(False, False)
    root.mainloop()