import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.listen()
scoreboard = Scoreboard()
turtle = Player()
car_manager = CarManager()

screen.onkey(turtle.go_up,"Up")
screen.onkey(turtle.go_down,"Down")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    if turtle.ycor() > 290 :
        scoreboard.score_refresh()
        turtle.reset_posicion()
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()
            