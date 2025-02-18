from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.shapesize(stretch_wid= 1, stretch_len=1)
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
    def reset_posicion(self):
        self.goto(STARTING_POSITION)
        