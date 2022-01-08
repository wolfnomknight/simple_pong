from turtle import Turtle

class GameScore(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.pencolor("white")
        self.goto(x, y)
        self.hideturtle()
        self.value = 0

    def plus_score(self):
        self.value += 1

    def show_score(self):
        self.clear()
        self.pendown()
        self.write(arg=self.value, move=False, align="center", font=("Courier", 42, "bold"))