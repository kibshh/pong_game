from turtle import Turtle


class Additional(Turtle):
    def __init__(self):
        super().__init__()
        self.create_additional()

    def create_additional(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(350, -370)
        self.write("Press 'q' to quit", align="center", font=("Courier", 15, "normal"))

    def additional_end(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Press anywhere on the screen to quit", align="center", font=("Courier", 20, "normal"))
