from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,x ,y):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.i= 0 
        self.goto(x,y)
        self.write(f"{self.i}", font= ("Courier", 20))

    def update_score(self):
        self.clear()
        self.i += 1
        self.write(f"{self.i}", font= ("Courier", 20))

    