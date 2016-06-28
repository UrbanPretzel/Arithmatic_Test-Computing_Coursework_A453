#Task 1 Controlled assessment - Conor Hennessy - Centre number: 10809 - November 2014
#Importing respective libraries
import random

##Defining function to generate two random numbers
FirstValue = 0
SecondValue = 0
def RandomNumbers():
    global FirstValue
    global SecondValue
    FirstValue = random.randint(1, 12)
    SecondValue = random.randint(1, 12)
    return (FirstValue, SecondValue)

##Defining RandomQuestion function to choose the question type
question = 0
ans = 0
def RandomQuestion():
    QuestionTypeNum = random.randint(1,3)
    global question
    global ans
    if QuestionTypeNum == 1:
        ##(The question will be a addition question)
        RandomNumbers()
        question = str(FirstValue)+str("+")+str(SecondValue)
        ans = FirstValue + SecondValue
        return (question)
    elif QuestionTypeNum == 2:
        ##(The question will be a subtraction question)
        RandomNumbers()
        question = str(FirstValue)+str("-")+str(SecondValue)
        ans = FirstValue - SecondValue
        return (question)
    else:
        ##(The question will be a multiplication question)
        RandomNumbers()
        question = str(FirstValue)+str("*")+str(SecondValue)
        ans = FirstValue * SecondValue
        return (question)

##Defining QuestionMarker function
#Setting start score to zero
score = 0
def QuestionMarker(ans, answer):
    global score
    if answer == ans:
        score = score + 1
        return (print ("Correct!\n"))
    else:
        return (print ("Incorrect.\n"))

#Function used to run the quiz when demanded by task two
def RunQuiz():
    ###Beginning the program; outputting the starting information and then the test.
    global name
    name = input("What is your name? ")
    print(name,"the test has begun.\nYou may not use a calculator for this test.\n")
    #Printing questions
    count = 0
    while count != 10:
        count = count + 1
        print("Question number", count,"out of ten:")
        #Returning an error message if their input is not an integer
        try:
            answer = int(input(RandomQuestion()+"="))
            QuestionMarker(ans, answer)
        except ValueError:
            print ("Your answer should be a number!\n")
    #Outputting their result
    print("\nThe test is now finished "+name+".")
    print("Your score is",score,"out of 10.")
    
#Prevent from running if this module is being imported by another module
if __name__ == '__main__':
    print(RunQuiz())

