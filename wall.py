from turtle import Turtle
import random


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks = []

        self.initial_x_post = -380
        self.initial_y_post = 250

        self.create_bricks()

    @staticmethod
    def randon_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color_rgb = (r, g, b)
        return color_rgb

    def create_bricks(self):
        for brick in range(221):
            new_brick = self.brick()
            self.bricks.append(new_brick)
            if (brick + 1) % 13 == 0:
                self.initial_y_post -= 20
                self.initial_x_post = -380
            else:
                self.initial_x_post += 61

    def brick(self):
        brick = Turtle("square")
        brick.penup()
        brick.color(self.randon_color())
        brick.shapesize(1, 3)
        brick.goto(self.initial_x_post, self.initial_y_post)
        return brick

    def destroy_brick(self, ball, score):
        for brick in self.bricks:
            if brick.distance(ball) < 25:
                # remove brick
                del self.bricks[0]
                brick.reset()
                brick.hideturtle()
                # bounce ball
                ball.brick_bounce()
                # increase ball speed
                ball.speed *= 0.98
                # increase score
                score.add_score()




