from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 1
        self.penup()
        self.goto(-200,265)
        self.color("black")
        self.hideturtle()
        self.write(f"Level: {self.x}",True, align= "center", font=FONT)
        
    def score_refresh (self):
        self.clear()
        self.goto(-200,265)
        self.x +=1
        self.write(f"Level: {self.x}",True, align= "center", font=FONT)
    
    def game_over(self):
        super().__init__()
        self.penup()
        self.goto(0,0)
        self.color("black")
        self.hideturtle()
        self.write("Game Over!",True, align= "center", font=("Arial", 24, "normal"))
        