from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)

screen.bgcolor("black")

screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Dectect collision with food

    if snake.head.distance(food) <15 :
            food.refresh()
            snake.extend()
            scoreboard.increment_score()

    #Detect collision with wall

    if snake.head.xcor() > 290 or snake.head.xcor()< -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail.
    for turtle in snake.turtles[1:]:

        if snake.head.distance(turtle)<10:
            scoreboard.reset()
            snake.reset()












screen.exitonclick()






