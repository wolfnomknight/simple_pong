from turtle import Turtle
import random


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.right(90)
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.computer_player_speed = 1

    def move_up(self):
        self.backward(20)

    def move_down(self):
        self.forward(20)

    def follow_ball(self, y):
        if y > self.ycor():
            self.goto(y=self.ycor() + self.computer_player_speed, x=300)
        if y < self.ycor():
            self.goto(y=self.ycor() - self.computer_player_speed, x=300)

    def random_movement(self):
        random_list = ["up", "down"]
        random_move = random.choice(random_list)
        if random_move == "up":
            self.goto(y=self.ycor() + self.computer_player_speed, x=300)
        elif random_move == "down":
            self.goto(y=self.ycor() - self.computer_player_speed, x=300)
