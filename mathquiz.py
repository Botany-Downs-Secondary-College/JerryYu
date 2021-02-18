# importing all modules from tkinter
from tkinter import * 
from random import randint, choice
from tkinter import ttk

# declare parent class called mathquiz. All objects created from parent class
class mathquiz:
    # use init method for all widgets
    def __init__(self, parent):
        
        self.quiz_machine = question_generator()
        
        # Default Frame
        self.default_frame = Frame(parent)
        self.default_frame.grid(row = 0, column = 0, sticky='nw')
        welcome_label = Label(self.default_frame, text="Welcome !", font = ("Time", '16', 'bold italic'))
        welcome_label.grid(row=0, column=0, sticky='w', padx = (7, 0), pady = (5, 0))
        welcome_info = Label(self.default_frame, text="Welcome to the Mathquiz that increases in difficulty as you proceed :)", wraplength= 250, justify="left")
        
        welcome_info.grid(row=1, column=0, sticky='w', padx = (7, 0), pady = (0, 10), columnspan = 1)
        
        self.default_frame2 = Frame(parent)
        self.default_frame2.grid(row = 1, column =0, sticky='w')
        name_info = Label(self.default_frame2, text = "Your Name :")
        name_info.grid(row=2, column=0, sticky='w', padx = (7, 0), pady = (0, 5))
        age_info = Label(self.default_frame2, text = "Your Age   :")
        age_info.grid(row=3, column=0, sticky='w', padx = (7, 0))
        self.name_entry = ttk.Entry(self.default_frame2)
        self.name_entry.grid(row = 2, column = 1, sticky='w')
        self.age_entry = ttk.Entry(self.default_frame2)
        self.age_entry.grid(row = 3, column = 1, sticky='w')
        start_button = ttk.Button(self.default_frame2, text = "start", width = 12)
        start_button.grid(row = 4, column = 1, pady = (4, 0), sticky='e')

        self.difficulty_choices = ["Easy", "Medium", "Hard"]
        self.alert_label = Label(self.default_frame2, text = "", fg = "Red")
        self.alert_label.grid(row = 5, column =0, sticky='w', pady = (7, 0), padx = (7,0))
        diff_label = Label(self.default_frame2, text = "choose your difficulty below:")
        diff_label.grid(row = 6, column=0, sticky='w', pady = (7, 0), padx = (7,0))
        
        self.diff_btns = []
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        for i in range(len(self.difficulty_choices)):
            rb = ttk.Radiobutton(self.default_frame2, variable = self.diff_lvl, value = i, text = self.difficulty_choices[i]) # , command = self.get_radio)
            self.diff_btns.append(rb)
            rb.grid(row = i+7, column = 1, sticky='w')

    def proceed_to_questions():
        pass # start page 2 here, page 2 = the page to start the quiz
        
        
'''
    def get_radio(self):
        print(self.difficulty_choices[int(self.diff_lvl.get())])

    def grab_questions(self):
        print(self.quiz_machine.get_math())
'''

class question_generator:
    def __init__(self):
        self.current_level = 1 
        self.operators = ['+', '-', '*', '/']
        self.max_num = 5
        self.quiz_number = 0
        self.quiz_correct = 0 # <---------- Variable not yet used, implementation coming in the future 

    def generate_quiz(self, lvl):
        #global self.current_level, self.max_num, self.quiz_number
        
        self.quiz_number += 1

        self.current_level = lvl
        self.base = ['self.current_quiz.append(str(randint(0, self.max_num)))', 'self.current_quiz.append(choice(self.operators))']
        self.current_quiz = []
        
        for level in range(1, lvl + 1):
            for item in self.base:
                exec(item)
        
        self.current_quiz.append(str(randint(0, self.max_num)))
        self.pen = ''.join(self.current_quiz)
        print(self.pen)
        
        if '/0' in self.pen: # If "divide by zero" is generated in the question, cancel the question and re-generate the question
            self.pen.replace('/0', f'{randint(1, self.max_num)}')
        
        self.answer = round(eval(self.pen), 2)
        
        return self.quiz_number, self.pen, self.answer

    def get_math(self):
        self.quizdata = self.generate_quiz(self.current_level)
        if self.quiz_number % 5 == 0: # Every five levels the difficulty increases by:
            self.current_level += 1   # One extra value in the question
            self.max_num += 5         # The max value in questions increase by 10
            
        return self.quizdata # Returns the important math quiz data to python



# Main routine

if __name__ == "__main__":
    root = Tk()
    frames = mathquiz(root)
    root.title("Math Quiz")
    root.geometry('400x400')
    root.resizable(False, False)
    root.mainloop()