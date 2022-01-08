from turtle import Turtle

class CentralLine(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=0.4, stretch_wid=70)
        self.penup()
        self.color("white")