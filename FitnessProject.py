# Fitness Program

"""

Specification:

- Set up a board with which a player is placed on one corner of it.
For example, a 5-by-5 board that looks like:
x   x   x   x   x
x   x   x   x   x
x   x   x   x   x
x   x   x   x   x
x   x   x   x   x

(2D Arrays)

list = [(1, 2), (1, 2)]

Potentially set it up so that the user can choose a colour at the start of the game
for their token.

(X)
(Y)
(Z)

(X) - Red
(X) - Blue
(X) - Green

- Each element should have a different activity written to it.
The format should look good, so the words should all be readable and
properly spaced apart.
E.g:

5 Press-Ups     5 Sit-Ups(X)10 Lunges
5 Star Jumps    |15 Squats| 20 Press-Ups
10 Burpees      7 Rotations 30 Side Lunges
etc.

- Random element to roll dice when prompted. The user should be shown
moving through the board.
Consider doing this with a COLOUR element, such as turning the text red
when the user is on it.

- Take user input as to whether they are doing the challenge or not.
If no, return the user to the previous space and they lose their turn.
If yes, keep the user on their current space and continue to the next turn.

- In concept, it is like Snakes and Ladders if, instead of snakes and ladders,
there are the fitness challenges. Failing the challenge results in a snake effect
of moving backwards.

"""

# Introduction

gameBoard = [""]

gameBoard = [("x", "x", "x", "x", "End"),
             ("x", "x", "x", "x", "x"),
             ("x", "x", "x", "x", "x"),
             ("x", "x", "x", "x", "x"),
             ("Start", "x", "x", "x", "x")]
