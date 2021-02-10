# simple version of math quiz without GUI, just to practice some functions
# 10/2/2021 Jerry

import random

current_level = 1
operators = ['+', '-', '*', '/']
max_num = 10
quiz_number = 0
quiz_correct = 0 # <---------- Variable not yet used, implementation coming in the future 

def error(code):
    global current_level, max_num
    generate_quiz(current_level, True)

def generate_quiz(lvl, from_error):
    global current_level, max_num, quiz_number
    
    if from_error == False: # Makes the quiz number remain the same if program occured with "divide with zero"
        quiz_number += 1

    current_level = lvl
    base = ['current_quiz.append(str(random.randint(0,max_num)))', 'current_quiz.append(random.choice(operators))']
    current_quiz = []
    
    for level in range(1, lvl + 1):
        for item in base:
            exec(item)
        
    current_quiz.append(str(random.randint(0,max_num)))
    pen = ''.join(current_quiz)
    
    if '/0' in pen: # If "divide by zero" is generated in the question, cancel the question and re-generate the question
        error(0)
        return
    
    print(f'Question No. [ {quiz_number} ]') # Display the question number
    print(f'what is [ {pen} ] equal to?') # The question
    print(f'Answer : [ {round(eval(pen), 2)} ]') # The answer

def mathquiz():
    global current_level, max_num, quiz_number
    while True:
        generate_quiz(current_level, False)
        temp = input('\n[press any key]\n')
        if quiz_number % 5 == 0: # Every five levels the difficulty increases by:
            current_level += 1   # One extra value in the question
            max_num += 10        # The max value in questions increase by 10

# A starter function that starts the program
mathquiz()