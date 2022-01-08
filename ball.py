from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.current_x_speed = 0.3
        self.current_y_speed = 0.3
        self.total_score = 0

    def ball_start(self):
        self.speed(0)
        self.goto(0, 0)
        self.total_score += 1
        if self.current_x_speed > 0:
            self.current_x_speed = -0.3 - (self.total_score / 20)
        elif self.current_x_speed < 0:
            self.current_x_speed = 0.3 + (self.total_score / 20)
        self.current_y_speed = 0.3 + (self.total_score / 20)

    def ball_move(self):
        self.new_x = self.xcor() + self.current_x_speed

        if self.ycor() >= 290 or self.ycor() <= -290:
            self.current_y_speed -= 0.1
            self.current_y_speed *= -1
        self.new_y = self.ycor() + self.current_y_speed

        self.goto(self.new_x, self.new_y)

    def hit_paddle(self):
        if self.current_x_speed > 0:
            self.current_x_speed += 0.2
        else:
            self.current_x_speed -= 0.2
        self.current_x_speed *= -1