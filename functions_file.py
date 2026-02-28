''' This file contains all the required functions '''
# importing the required files or libraries
import random

# this function finds out all the multiples of a given number and is used to make a division quiz possible
def find_multiples(ele1): 
    multiples = [] 
    for i in range(1, ele1 + 1): 
        if ele1 % i == 0: 
            multiples.append(i) 

    return multiples

# this function generates the quiz
def quiz_generator():
    curr_operator = random.choice(["+", "-", "X", "÷"])    

    ele1, ele2 = 0, 0

    if curr_operator == "+":
        ele1 = random.randint(1, 101)
        ele2 = random.randint(1, 101)
    
    elif curr_operator == "-":
        ele1 = random.randint(1, 101)
        ele2 = random.randint(1, 101)

    elif curr_operator == "X":
        ele1 = random.randint(1, 51)
        ele2 = random.randint(1, 31)

    else:
        ele1 = random.randint(1, 101)
        ele2 = random.choice(find_multiples(ele1))

    return [ele1, curr_operator, ele2]

# this function calculates the answer of the curr quiz so as match the answer of user with the correct answer
def calculate_answer(curr_quiz):
    answer = 0

    if curr_quiz[1] == "+":
        answer = curr_quiz[0] + curr_quiz[2]

    elif curr_quiz[1] == "-":
        answer = curr_quiz[0] - curr_quiz[2]

    elif curr_quiz[1] == "X":
        answer = curr_quiz[0] * curr_quiz[2]

    else:
        answer = int(curr_quiz[0] / curr_quiz[2])

    return answer
