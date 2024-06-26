from turtle import Turtle
INITIAL_POSITION = (0, 0)


class Paddle(Turtle):
    def __init__(self, shape, color):
        super().__init__()
        # Initial setup
        self.shape(shape)
        self.color(color)
        self.shapesize(stretch_len=6)
        self.penup()
        self.goto(0, -280)
