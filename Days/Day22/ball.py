import random
import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.move_x = 5
        self.move_y = 5

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def move_logical(self, angle):
        print(angle)
        self.setheading(angle)
        self.forward(10)

    def bounce(self):
        self.move_y *= -1

    def hit(self):
        self.move_x *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.hit()
        time.sleep(1)