# from turtle import Turtle, Screen
import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)

t.shape("classic")
t.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Draw a rectangle
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw a straight dashed line
for _ in range(10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


# Draw 10 different shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for shape_size_n in range(3, 11):
    t.color(random_color())
    draw_shape(shape_size_n)


# Random walk
directions = [0, 90, 180, 270]
t.pensize(10)
for _ in range(1000):
    t.forward(30)
    t.color(random_color())
    t.setheading(random.choice(directions))

# Draw a Spiral


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
