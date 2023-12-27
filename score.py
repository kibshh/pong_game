from turtle import Turtle


class Score(Turtle):
    def __init__(self, starting_pos):
        super().__init__()
        self.score = 0
        self.position = starting_pos
        self.create_score()

    def create_score(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(self.position)
        self.write(self.score, align="center", font=("Courier", 80, "bold"))

    def score_refresh(self):
        self.clear()
        self.create_score()
