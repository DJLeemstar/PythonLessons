#Lexi 2 Hour Monday Lesson :)
#13/04/2020
#Debugging & It's Connection w/ Files

import traceback

# Theory - Proper Debugging Practise
# - "Unoptimal group practise is better than optimal singular practise"
# - Dealing with 'bad code'
# - Make sure to comment, but don't comment TOO much
# - Be careful only with what's important. Otherwise, you're performing unnecessary checks

# Further Learning : "ProjectLearn.io"
# Perhaps a bit extreme for your current level, but very interesting to read

'''

Prospectus::
 - Debug Window & How To Use It (Start Debugging and then Add Window)
 - Try/Except
 - Creating a File
 - Reading From/Writing To a File
 - Creating an Error Log

We'll see how much we get done - anything that isn't done can potentially be used in a future lesson.

# Black box Testing
# White Box Testing
# Beta/Alpha Testing

string = "Hello"
int = 1
float = 1.2

#Syntax Error
#int = int + "hello"

#Logic Error
#int = int + 2
'''
def testProcedure():
    functionInt = 0
    print("FunctionInt will be changed!")
    functionInt = 1
    print("FunctionInt has been changed!")

print("The program has begun!")
print("The program stopped just before executing the last 'print' statement!")
print("That's because of the breakpoint (red dot) next to it.")

int = 2

testProcedure()     # Pressing 'f8' here is different to pressing 'f7'.
                    # These two tools (f7 and f8) are similar, but different!

print("After stepping into that procedure, notice how the watch takes note of the effects?")
print("We can see how watches and breakpoints both serve to whittle down the failures of a program.")

int = 3

print("There are a wide variety of debug tools inside of Pycharm and other programs.\n")



ourFile = open("file.txt","w+")     # '+' at the end indicates read AND write
                                    # By using 'w', the file will be created should it be found to not exist

ourFile.write("This is our written line!")

ourFile.close()                     # Always close a file after it has been used!
                                    # If a file stream is open, then the file can't be accessed 
                                    # by other sources!

# 'a' mode is Append Mode
ourFile = open("file.txt","a+") 

ourFile.write("We have appended some text!")
ourFile.write("\nWe have appended more text!")
ourFile.close()

# Something a bit different -- 'Try' and 'Except'
try:
    ourFile = open("file.txt", "r")
    print(ourFile.read())
    ourFile.close()

    # Observe what happens if we remove the 'close()'

    ourFile = open("file.txt", "r")
    Lines = ourFile.readlines()
    for line in Lines:
        print(line)
    ourFile.close()

# Checks for filenotfound errors
except ourFile:
    print("That file does not exist!")

    errorLog = open("ErrorFile.txt", "w")
    errorLog.write(traceback.format_exc())
    errorLog.close()

# Highscore System:
# User inputs a value
# Value is saved to a notepad file, each value saved on a separate line
# If file is not found, create it
# Try to not use the 'w' option to create a file until you have checked that you get an error when accessing the file
# Bonus: Sort the numbers in the file so they're from highest to lowest















