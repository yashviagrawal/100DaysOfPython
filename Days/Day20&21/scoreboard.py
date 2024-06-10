from turtle import Turtle
ALIGN = "center"
FONT = ("chalkduster", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.pendown()
        self.high = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"SCORE: {self.score}    HIGH SCORE: {self.high}", False, ALIGN, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}    HIGH SCORE: {self.high}", False, ALIGN, FONT)

    def gameover(self):
        self.clear()
        self.pencolor("red")
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER", False, ALIGN, FONT)
        self.pencolor("white")
        self.penup()
        self.goto(0, -40)
        self.pendown()
        self.write(f"SCORE: {self.score}    HIGH SCORE:{self.high}", False, ALIGN, FONT)

    def reset(self):
        self.clear()
        if self.score > self.high:
            self.high = self.score
            self.update_board()
            self.score = 1
