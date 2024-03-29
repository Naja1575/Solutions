"""
Exercise "Tom the Turtle":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

The function "demo" introduces you to all commands you need to interact with Tom in the following exercises.

Only if you are curious and love details:
    Here is the full turtle graphics documentation:
    https://docs.python.org/3.3/library/turtle.html

Part 1:
    Write a function "square" which accepts a parameter "length".
    Calling this function causes the turtle to draw a square with a side length of "length" pixels.

Part 2:
     Write a function "visible" which returns a boolean value,
     indicating if the turtle is in the visible area of the screen.
     Use this function in the following parts of this exercise
     to return the turtle to the screen when it wandered off.

Part 3:
    Write a function "many_squares" with a for loop, which calls square repeatedly.
    Use this function to draw several squares of different sizes in different positions.
    The function shall have some parameters. For example:
        number: how many squares will be drawn?
        size: how large are the squares?
        distance: how far away from the last square is the next square positioned?

Part 4:
    Write a function that produces patterns similar to this:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Part 5:
    Write a function that produces patterns similar to this:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    The function shall have a parameter, that influences the shape of the pattern.

Part 6:
    Create your own function that produces a cool pattern.
    Later, if you like, present your pattern on the big screen to the others.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""


import turtle    # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.


def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):
        tom.forward(100)  # move 100 pixels
        tom.left(45)  # turn 45 degrees left
        print("Tom is now at", tom.position())
    tom.penup()  # do not draw while moving
    tom.forward(222)
    tom.pendown()  # draw while moving
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(333)
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done

def square(one, length):
    one.speed(6)
    for x in range(4):
        one.forward(length)
        one.left(90)
        print(visible(one))
        if not visible(one):
            home(one)

def visible(turtle):
    hey = turtle.position()
    print(hey[0], hey[1])
    return -300 < hey[0] < 300 and -300 < hey[1] < 300

def home(two):
    two.penup()
    two.home()
    two.pendown()

def many_squares(one, lenght, squares):
    for s in range(squares):
        lenght = (s + 1) * lenght
        square(one, lenght)
        one.penup()
        one.forward(90)
        one.pendown()


def pattern(tom, ran, ron):
    tom.speed(10)
    for i in range(ran):
        tom.forward(ron * i)
        tom.left(90)


def star(tom, side, lenght):
    tom.speed(8)
    for i in range(side):
        tom.forward(lenght)
        angle = (180 / side)
        tom.left(180 - angle)
        print(angle)


tom = turtle.Turtle()  # create an object named tom of type Turtle
# visible(tom)
# square(tom, 1000)
# many_squares(tom, 20, 3)
# pattern(tom, 20, 20)
star(tom, 25, 200)
turtle.done()