from screen import MainScreen
from paddle import Paddle
from ball import Ball

screen = MainScreen()
paddle = Paddle()
ball = Ball()

while True:
    screen.mainscreen.update()
    ball.move()