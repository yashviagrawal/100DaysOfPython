from turtle import Screen
from turtle import Turtle
import time

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for i in range(0, 3):
            self.s = Turtle("square")
            self.s.color("white")
            self.s.penup()
            self.s.speed(1)
            self.s.setx(i * -20)
            self.snake_body.append(self.s)
            self.head = self.snake_body[0]

    def add_tail(self):
        self.s = Turtle("square")
        self.s.speed(0)
        self.s.color("white")
        self.s.penup()
        self.snake_body.append(self.s)


    def move(self):
        for block_num in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[block_num].goto(self.snake_body[block_num - 1].xcor(), self.snake_body[block_num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
