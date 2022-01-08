from turtle import Screen


class GameScreen(Screen):
    def __init__(self):
        super().__init__()
        self.title("Pong")
        self.bgcolor("black")
        self.setup(width=800, height=600)
        self.tracer(0)
    
    def game_play(self):
       self.tracer(1)
       self.listen()
       # self.onkeypress(player.move_up, "Up")
       # self.onkeypress(player.move_up, "w")
       # self.onkeypress(player.move_down, "Down")
       # self.onkeypress(player.move_down, "s")
       self.exitonclick()