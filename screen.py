from turtle import Screen, Turtle


class MainScreen:
    def __init__(self):
        self.mainscreen = Screen()
        self.mainscreen.bgcolor("green")
        self.mainscreen.setup(height=400, width=500)
        self.mainscreen.title("Breakpoint Game")
        self.mainscreen.tracer(0)