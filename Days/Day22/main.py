from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.listen()
screen.title("PONG GAME")
screen.tracer(0)

player_r = Paddle((350, 0))
player_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(player_r.up, "Up")
screen.onkey(player_r.down, "Down")
screen.onkey(player_l.up, "w")
screen.onkey(player_l.down, "s")
play = True

while play:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if (ball.distance(player_r) < 50 and ball.xcor() > 320) or (ball.distance(player_l) < 50 and ball.xcor() > -350):
        ball.hit()
        # ball.move_y -= 1
        # ball.move_x -= 1
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.left_score()
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_score()

screen.exitonclick()