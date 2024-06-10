import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crosser")

player = Player()
score = Scoreboard()
car = Car()
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
play = True

while play:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            score.game_over()
            play = False

    if player.has_crossed():
        car.level_up()
        score.update_board()

screen.exitonclick()