from turtle import Turtle
import config


class Paddle(Turtle):
    def __init__(self, starting_cor, color):
        super().__init__()
        self.starting_pos = starting_cor
        self.paddle_color = color
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color(self.paddle_color)
        self.shapesize(5, 1)
        self.penup()
        self.goto(self.starting_pos)

    def up(self):
        new_y = self.ycor() + 25
        if new_y < (config.SCREEN_HEIGHT / 2 - 40):
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 25
        if new_y > (-(config.SCREEN_HEIGHT / 2) + 40):
            self.goto(self.xcor(), new_y)
