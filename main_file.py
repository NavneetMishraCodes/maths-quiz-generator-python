# importing required files or libraries 
import random 
import time
import functions_file as fnf

# introducing the maths quiz generator
print("Welcome! To The Maths Quiz Generator...")
print("To exit, type '-99999' as answer to a quiz/question.")
print() # for separation

# required variables
quiz_count = 1
score = 0

# main generator loop
while True:
    curr_quiz = fnf.quiz_generator()

    # printing score
    print(f"Current Score: {score}")

    # printing the quiz for the user
    print(f"Quiz No.{quiz_count}: {curr_quiz[0]} {curr_quiz[1]} {curr_quiz[2]}")

    # getting answer from the calculate answer function in fnf
    curr_answer = fnf.calculate_answer(curr_quiz)

    # taking input from the user
    user_input = None 
    
    try:
        user_input = int(input("Your answer: "))
    except ValueError:
        print("Invalid Input !!")
        print("Restart the program to play again...")
        print("Exiting...")
        time.sleep(8)
        exit()    

    # checking the user input
    if user_input == -99999:
        print("Exiting...")
        time.sleep(5)
        exit()
    
    else:
        if user_input == curr_answer:
            print("Correct answer :) ")
            print("Score + 10")
            score += 10

        else:
            print("Wrong answer :( ")
            print("Score - 5") 
            score -= 5       

    quiz_count += 1
    print()    

