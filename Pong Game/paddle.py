from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.color("white")
        self.penup()
        self.goto(x,y)

    def move_up(self):
        y_cornew = self.ycor()  + 20
        self.goto(self.xcor(), y_cornew)

    def move_down(self):
        y_cornew = self.ycor() - 20
        self.goto(self.xcor(), y_cornew)