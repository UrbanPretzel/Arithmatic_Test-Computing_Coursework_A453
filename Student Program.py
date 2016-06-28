#---
import Test

##Defining RunTest function to run task one code 
def RunTest():
    Test.RunQuiz()
    
##Defining Savescore function with code to check for headers and get values from test 
def Savedata():
    print("Writing to file...")
    global data
    data = [{'Name':name,'Score':score,'Class':classSet}]
    global fileHandle
    try:
        open(str(classSet)+' Class Results.csv', 'r')
        header = 'yes'
        if header == 'yes':
            fileHandle = open(str(classSet)+' Class Results.csv', 'a')
            WriteToFile()
    except IOError:
        fileHandle = open(str(classSet)+' Class Results.csv', 'a')
        fileHandle.write('Name,Score\n')
        WriteToFile()

##Defining WriteToFile function
def WriteToFile():
    for value in data:
        fileHandle.write('{Name},{Score}'.format(**value))
    fileHandle.write('\n')
    fileHandle.close()
    print ("Writing to file complete!")

# Function asking what class they are in
def ClassChecker():
    global classSet
    classSet = input ("What is your class set? ")
    if classSet == 'x1' or classSet == 'x2' or classSet == 'x3':
        return '\n'
    else:
        print("[Please input in the form: x1, x2 or x3]")
        return ClassChecker()

#Running the test and then writing the score to file
ClassChecker()
if __name__ == '__main__':
    RunTest()
    from Test import name, score
    Savedata()

