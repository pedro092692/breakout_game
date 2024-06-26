from turtle import Screen
from ball import Ball
from paddle import Paddle
from lives import Lives
from wall import Wall
import time


class Game:
    def __init__(self, title: str, size, bg):
        # screen setup
        self.screen = Screen()
        self.screen.setup(width=size[0], height=size[1])
        self.screen.title(title.upper())
        self.screen.colormode(255)
        self.screen.bgcolor(bg)
        self.screen.tracer(0)

        # game setup
        self.lives = Lives()
        self.paddle = Paddle(shape='square', color='blue')
        self.ball = Ball(shape='circle', color='red', parent=self)
        self.wall = Wall()

        # move paddle
        self.screen.listen()
        self.screen.onkeypress(key='Right', fun=self.paddle.move_right)
        self.screen.onkeypress(key='Left', fun=self.paddle.move_left)

    def play_game(self):
        while True:
            time.sleep(self.ball.speed)
            self.screen.update()

            # detect collision with walls
            self.ball.ball_bounce()

            # move ball
            self.ball.move_ball()
            self.ball.paddle_bounce(paddle=self.paddle)

            # destroy brick
            self.wall.destroy_brick(ball=self.ball)

            if self.lives.lives < 0:
                self.lives.game_over()
                return

