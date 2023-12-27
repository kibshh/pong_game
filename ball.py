from turtle import Turtle
from random import randint
import config


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 2
        self.y_move = 2

    def create_ball(self):
        self.goto(0, 0)
        self.color(config.BALL_COLOR)
        self.shape("circle")
        self.penup()

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collision_with_wall(self):
        self.y_move *= -1

    def collision_with_paddle(self):
        self.x_move *= -config.DIFFICULTY
        self.y_move *= config.DIFFICULTY

    def reset_pos(self):
        self.create_ball()
        self.x_move = 2
        self.y_move = 2
        rand_num = randint(1, 4)
        if rand_num == 1:
            self.x_move *= -1
        elif rand_num == 2:
            self.y_move *= -1
        elif rand_num == 3:
            self.x_move *= -1
            self.y_move *= -1
        else:
            pass
