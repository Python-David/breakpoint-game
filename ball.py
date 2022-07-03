from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("#BC4749")
        self.ball.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.ball.penup()

    def move(self):
        new_x = self.ball.xcor() + 1
        new_y = self.ball.ycor() + 1
        self.ball.goto(new_x, new_y)