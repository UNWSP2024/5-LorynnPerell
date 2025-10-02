# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------
import random

randomNumber1 = random.randint( 2,607 )
randomNumber2 = random.randint( 2,607 )

def askQuestion():
    global randomNumber1
    global randomNumber2

    userAnswer = int( input( "What is " + str( randomNumber1 ) + " + " + \
               str( randomNumber2 ) + "?: "))
    return userAnswer
    
def checkAnswer( userAnswer ):
    global randomNumber1
    global randomNumber2

    correctAnswer = randomNumber1 + randomNumber2
    print()
    if userAnswer == correctAnswer:
        print("Congradulations! you got it correct!")
    else:
        print("Your answer is wrong. The correct answer is", correctAnswer )

def main():
    userAnswer = askQuestion()
    checkAnswer( userAnswer )

main()

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.