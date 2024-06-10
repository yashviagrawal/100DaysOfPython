from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.color("gray")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.penup()
        self.goto(0, 250)
        self.pendown()
        self.goto(0, -250)
        self.penup()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def left_score(self):
        self.l_score += 1
        self.update_board()

    def right_score(self):
        self.r_score += 1
        self.update_board()