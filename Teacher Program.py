# Importing python modules
import csv
import operator

# Putting the data into a dictionary
def FileZipper():
    with open (str(classset)+" Class Results.csv","r") as record:
        lines = record.readlines()[1:]
        global classData
        classData = []
        for row in lines:
            student = row.split(",")
            Headers = ['name','test 1','test 2','test 3']
            data = zip(Headers,student)
            classDataDict = dict (data)
            classData.append(classDataDict)
        return classData

##Functions for manipulating the data in the CSV files  for sorting the data)
#Function to sort names alphabetically in the list of dictionary
def ClassNameSort():
    classData.sort(key = operator.itemgetter('name'))
    print("\n-----  Class names sorted alphabetically -----")
    for student in classData:
        print (student['name'],student['test 1'],student['test 2'],student['test 1'])
    print ("\n")

#Function to output the average test score for each student
def studentAdverageScore():
    print("\n-----  Average score for each student -----")
    for student in classData:
        student['ScoreAdverage'] = (int(student['test 1']) + int(student['test 2']) + int(student['test 3']))//3
    classData.sort(key = operator.itemgetter('ScoreAdverage'))
    classData.reverse()
    for student in classData:
        print (student['ScoreAdverage'],student['name'])        
    print ("\n")
    
#Function to output the  highest score from the three tests for each student
def ClassHighestScore():
    print("\n-----  students Highest score overall -----")
    for student in classData:
        student['HighestScore'] = max(int(student['test 1']),int(student['test 2']),int(student['test 3']))
    classData.sort(key = operator.itemgetter('HighestScore'))
    classData.reverse()
    for student in classData:
        print (student['HighestScore'],student['name'])
    print ("\n")

#Function to Print the Class data in a dictionary within a List
def ClassOutput():
    print("\n-----  Class data in a dictionary within a List -----")
    print (classData)
    print ("\n")

    
## Defining the TeacherMenu function to run the test for the user
def TeacherMenu():
    #Output main menu options since they are a teacher
    print ("\n----------  TEACHER MAIN MENU  ----------")
    print ("""Available options:
             1) Show the stored data for a class \n
             2) Show the data for a class in alphabetical order with their highest result\n
             3) Show the highest test score for each student in a class (Highest to lowest)\n
             4) Show the average score for each student in a class (Highest to lowest)""")

    #Ask teacher for choice and ensure it is relevant
    def ChoiceChecker():
        global choice
        choice = input("\nWhat option would you like to select? ")
        #Input handling code to ensure their input is one of the choices from the menu
        if choice == '1' or choice == '2' or choice == '3' or choice == '4':
            return '\n'
        else:
            print("[Please input in the form: 1, 2, 3 or 4]")
            return ChoiceChecker()
    ChoiceChecker()

    #Defining a function for asking what class to use when sorting
    def ClassChecker():
        global classset
        classset = input ("What class would you like to select? ")
        if classset == 'x1' or classset == 'x2' or classset == 'x3':
            return '\n'
        else:
            print("[Please input in the form: x1, x2 or x3]")
            return ClassChecker()
    ClassChecker()

    #Outputting depending on teacher choice
    FileZipper()
    if choice == '1':
        ClassOutput()
    elif choice == '2':
        ClassNameSort()
    elif choice == '3':
        ClassHighestScore()        
    else:
        studentAdverageScore()

#Run the main menu function to run the program with different outputs for teachers and students
MainMenu()
