from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("#BC4749")
        self.ball.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.ball.penup()
        self.x_move = 1
        self.y_move = 1

    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1