from turtle import Turtle
INITIAL_POSITION = (0, 0)


class Paddle(Turtle):
    def __init__(self, shape, color):
        super().__init__()
        # Initial setup
        self.shape(shape)
        self.color(color)
        self.shapesize(1.33, 5)
        self.penup()
        self.goto(0, -280)

    def move_right(self):
        if self.xcor() < 340:
            new_x_cor = self.xcor() + 20
            self.goto(new_x_cor, self.ycor())

    def move_left(self):
        if self.xcor() > -340:
            new_x_cor = self.xcor() - 20
            self.goto(new_x_cor, self.ycor())

