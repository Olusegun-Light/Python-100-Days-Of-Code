from turtle import Turtle, Screen
from snake import Snake
import time

# Screen setup and creating snake body
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

# Listen To Arrow Keys on The Keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Move Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
