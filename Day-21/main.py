from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

# Screen setup and creating snake body
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect Collision With Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

        # Detect collision with Tail
        for segments in snake.segments[1:]:
            if snake.head.distance(segments) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
