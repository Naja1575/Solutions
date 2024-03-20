import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set up the turtle
artist = turtle.Turtle()
artist.speed(0)  # Set the speed of the turtle to the fastest


# Function to create colorful art
def colorful_art():
    for _ in range(100):
        # Choose a random color
        r = random.random()
        g = random.random()
        b = random.random()
        artist.color(r, g, b)

        # Choose a random pen size
        # pen_size = random.randint(1, 10)
        # artist.pensize(pen_size)
        artist.pensize(5)

        # Move the turtle in a random direction
        artist.forward(200)
        artist.right(260)


def colorful_spiral():
    for i in range(300):
        # Choose a random color
        r = random.random()
        g = random.random()
        b = random.random()
        artist.color(r, g, b)

        fw = i + 100

        # Draw a line and turn the turtle
        artist.forward(fw)
        artist.right(121)  # Adjust the angle for the spiral


# Function to draw a colorful spiral like a snail
def snail_spiral():
    length = 1
    angle = 20  # Adjust the turning angle to create a snail-like spiral
    for _ in range(100):
        # Choose a random color
        r = random.random()
        g = random.random()
        b = random.random()
        artist.color(r, 1, 0.63)

        # Draw a line and turn the turtle
        artist.forward(length)
        artist.right(angle)
        length += 1  # Increase the length for the next iteration


# Function to draw a petal
def draw_petal(size, width):
    angle = 180 - width
    artist.circle(size, width)
    artist.left(angle)
    artist.circle(size, width)
    artist.left(angle)


def colorr(red, green, blue, p):
    r = red
    g = green
    b = blue
    for i in range(p):
        if r > 0.1:
            r = r - 0.1
            artist.color(r, g, b)
        elif g > 0.1:
            g = g - 0.1
            artist.color(r, g, b)
        elif b > 0.1:
            b = b - 0.1
            artist.color(r, g, b)
        else:
            r = red
            g = green
            b = blue
            artist.color(r, g, b)


# Function to draw a flower
def draw_flower(s, w, p, r, g, b):
    artist.pensize(6)
    a = 360 / p

    for i in range(p):
        colorr(r, g, b, p)
        draw_petal(s, w)
        artist.right(a)



# Draw the colorful art
# colorful_art()
# colorful_spiral()
# snail_spiral()
draw_flower(150, 110, 10, 0.9, 0.4, 0.6)
# draw_petal()


# Hide the turtle
artist.hideturtle()

# Keep the window open
turtle.done()
