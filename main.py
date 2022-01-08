from turtle import Screen
import random
import paddle
import ball
import central_line
import game_score


screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

ball = ball.Ball()
central_line = central_line.CentralLine()

player_score = game_score.GameScore(-100, 220)
computer_score = game_score.GameScore(100, 220)
player_score.show_score()
computer_score.show_score()

player = paddle.Paddle(x=-300, y=0)
computer_player = paddle.Paddle(x=300, y=0)

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.ball_move()
    control = 0

    if control == 0:
        if ball.xcor() <= -280 or ball.xcor() >= 280:
            if ball.distance(player) < 50 or ball.distance(computer_player) < 50:
                ball.hit_paddle()

    while control > 0:
        if control == 1000000000:
            control = 0
        else:
            control += 1

    if ball.xcor() > 400:
        player_score.plus_score()
        player_score.show_score()
        ball.ball_start()
    elif ball.xcor() < -400:
        computer_score.plus_score()
        computer_score.show_score()
        ball.ball_start()

    variable_speed = [0.1, 0.2, 0.3, 0.4]
    random_speed = random.choice(variable_speed)
    if ball.xcor() > 0:
        if player_score.value > 0:
            computer_player.computer_player_speed = player_score.value * random_speed
        else:
            computer_player.computer_player_speed = random_speed
        computer_player.follow_ball(ball.ycor())
    else:
        computer_player.computer_player_speed = random_speed * 3
        computer_player.random_movement()
    if player_score.value > 3 or computer_score.value > 3:
        game_is_on = False

screen.exitonclick()
