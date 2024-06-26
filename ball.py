from turtle import Turtle
STARTING_POSITION = (0, -250)


class Ball(Turtle):
    def __init__(self, shape, color, parent):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.parent = parent

        # initial setup
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.speed = 0.1
        self.goto(STARTING_POSITION)

    def move_ball(self):
        new_x_cor = self.xcor() + self.move_x
        new_y_cor = self.ycor() + self.move_y
        self.goto(new_x_cor, new_y_cor)

    def ball_bounce(self):
        if self.ycor() > 280:
            self.move_y *= - 1

        if self.xcor() > 380 or self.xcor() < -380:
            self.move_x *= -1

        if self.ycor() < -280:
            self.ball_out()

    def paddle_bounce(self, paddle):
        if self.distance(paddle) < 37:
            self.move_y *= - 1
            print('bounce')

    def ball_out(self):
        self.goto(STARTING_POSITION)
        # reset y to positive move
        self.move_y *= -1
        self.parent.lives.subtract_lives()
