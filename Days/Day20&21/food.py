from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed(0)
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def drop_food(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))