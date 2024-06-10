from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        if random.randint(1, 6) == 1:
            self.s = Turtle()
            self.s.shape("square")
            self.s.shapesize(1, 2)
            self.s.penup()
            self.s.color(random.choice(COLORS))
            self.s.setheading(180)
            self.s.goto(300, random.randint(-250, 250))
            self.all_cars.append(self.s)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
       self.car_speed += MOVE_INCREMENT