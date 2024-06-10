from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed(0)
        self.color("white")
        self.penup()
        self.goto(position)


    def up(self):
        goto_y = self.ycor() + 20
        self.goto(self.xcor(), goto_y)

    def down(self):
        goto_y = self.ycor() - 20
        self.goto(self.xcor(), goto_y)
