# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------
def generate_quiz():
    num1 = 59
    num2 = 66
    return num1, num2
def math_quiz():
    num1, num2 = generate_quiz()
    print(f" {num1}")
    print(f"+ {num2}")
    print("------")
try:
    user_answer = int(input("Enter your answer: "))
except ValueError:
    print("Invalid input. Please enter a numeric value. ")
    
correct_answer = 125
if user_answer == correct_answer:
    print("Congradulations! Your answer is correct!")
else:
    print(f"Sorry! The correct answer is 125.")
if __name__ == "__main__":
    math_quiz()


# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.