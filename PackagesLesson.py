
import sys
import pygame
import pyperclip

#upper, isupper
#lower, islower

string = "AAA".lower()
print(string)

#Scope Creep

string = "Hello World"
spam = string[2]
print(spam)

#H e l l o   W o r l d
#0 1 2 3 4 5 6 7 8 9 10

list = [1, 2, 3, 4]
#       0, 1, 2, 3
print(list[0])
index = list.index(1)
#.index() == "search values for index
print(index)

list = ["Liam", "Steven", "Carl"]
#       0       1         2
print(list[1])
print(list.index("Carl"))


if "Hello" in string:
    print("It worked!")

name = "Liam"

#f-strings
print(f"My name is {name}, nice to meet you!")
print("My name is " + name + ", nice to meet you! How was your day?")

# isalpha - Returns True if there are only letters in the string
# isalnum - Returns True if there are only letters and numbers
# isdecimal - Returns True if there are only numbers
# isspace - Returns True if there are only spaces, tabs, and newlines
# istitle - Returns True if every string begins with an uppercase letter followed by
            # a lowercase letter

# Split and join

joinExample = ' space '.join(["1", "2", "3"])

splitExample = 'My%%%Name%%%Is%%%Console'.split("%%%")

print(joinExample)

print()

for i in splitExample:
    print (i)


#ASCII

print(ord('A'))     #'A' is equal to 65
print(chr(65))      #65 is equal to the character 'A'

'''
Project Concept: "Clipboard Carrier"

- When writing messages or emails, you might find yourself writing the same messages
over and over again.

- So, for someone in that position, it might be helpful to have a program that allows
you to enter certain 'Key Words' so that you can copy a phrase to your clipboard.

- However, how might you copy something to your clipboard?
The feature isn't directly supported in Python, so we'll need to use certain PACKAGES.

'''
import pyperclip
pyperclip.copy('The text to be copied to the clipboard.')


pygame.init()

size = width, height = 1080, 720
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("yugi.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
