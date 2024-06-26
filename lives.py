from turtle import Turtle
FONT = ('helvetica', 16, 'normal')
ALIGNMENT = 'center'
STARTING_POSITION = (-360, 270)


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(STARTING_POSITION)
        self.lives = 4
        # start
        self.subtract_lives()

    def subtract_lives(self):
        self.clear()
        self.lives -= 1
        self.write(f'lives: {self.lives}', align=ALIGNMENT, font=FONT)
