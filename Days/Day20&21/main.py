from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game`")
screen.tracer(0)
screen.listen()

# setting snake
tim = Snake()
#setting food
apple = Food()
#setting scoreboard
score = Scoreboard()


# setting keys
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.left, "Left")
screen.onkey(tim.right, "Right")

i = 0
play = True
while play:
    tim.move()
    screen.update()
    time.sleep(0.1)
    if tim.head.distance(apple) < 15:
        apple.drop_food()
        score.increase_score()
        tim.add_tail()
    if tim.head.xcor() > 280 or tim.head.xcor() < -280 or tim.head.ycor() > 280 or tim.head.ycor() < -280:
        score.reset()
    body = tim.snake_body[1:]
    for block in body:
        if tim.head.distance(block) < 10:
            score.reset()

screen.exitonclick()