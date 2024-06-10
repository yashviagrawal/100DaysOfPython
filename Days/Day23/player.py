from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape("turtle")
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.back(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def has_crossed(self):
        if self.ycor() > FINISH_LINE_Y:
            self.go_to_start()
            return True
        else: return False