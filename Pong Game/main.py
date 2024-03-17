from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

big_line = Turtle("square")
big_line.shapesize(stretch_wid= 30, stretch_len= 0.2)
big_line.goto(0,0)
big_line.color("white")

paddle = Paddle(x = 350, y = 0)
paddle_2 = Paddle(x = -350, y = 0)
ball = Ball()
left_score = Scoreboard(-100, 250)
right_score = Scoreboard(100,250)


screen.listen()
screen.onkey(paddle.move_up,"Up")
screen.onkey(paddle.move_down,"Down")
screen.onkey(paddle_2.move_up,"w")
screen.onkey(paddle_2.move_down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()
    
    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:        
        ball.bounce_off_paddle()
        
    
    if ball.xcor() > 380:  
        left_score.update_score()
        ball.reset_and_opposite()

    
    if ball.xcor() < - 380:
        right_score.update_score()
        ball.reset_and_opposite()
    
    



screen.exitonclick()