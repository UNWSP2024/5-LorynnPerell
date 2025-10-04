# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------
import random


def math_quiz():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    print(f"\n  {num1}")
    print(f"+ {num2}")
    print("------")
    try:
        user_answer = int(input("Your answer: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    correct_answer = num1 + num2
    if user_answer == correct_answer:
        print("Congratulations! That's correct.")
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")
def main():
    math_quiz()

main()
# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.