from screen import MainScreen
from paddle import Paddle
from ball import Ball

screen = MainScreen()
paddle = Paddle()
ball = Ball()

while True:
    screen.mainscreen.update()
    ball.move()

    #Detect Collision with Wall
    if ball.ball.ycor() > 188:
        ball.bounce_y()
    elif ball.ball.xcor() > 230 or ball.ball.xcor() < -240:
        ball.bounce_x()

    #Detect collision with paddle
    if ball.ball.distance(paddle.paddle) < 50 and ball.ball.ycor() < -167:
        ball.bounce_y()


