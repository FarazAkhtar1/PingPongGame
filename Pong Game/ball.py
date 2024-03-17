from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(0,0)
        self.color("white")
        self.move_ball_by_x = 10
        self.move_ball_by_y = 10
        self.move_speed = 0.1


    def move_ball(self):        
        self.goto(self.xcor() + self.move_ball_by_x, self.ycor() + self.move_ball_by_y)

    def bounce(self):
        self.move_ball_by_y *= -1

    def bounce_off_paddle(self):
        self.move_ball_by_x *= -1
        self.move_speed *= 0.9
    
    def reset_and_opposite(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.move_ball_by_x *= -1
        self.move_ball()
