from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("#F2E8CF")
        self.paddle.shapesize(stretch_wid=0.5, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -180)
        self.paddle.speed(0)
        self.paddle.ondrag(self.paddle_move)

    def paddle_move(self, x, y):
        self.paddle.ondrag(None)
        self.paddle.setx(x)
        self.paddle.ondrag(self.paddle_move)