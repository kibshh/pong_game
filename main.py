from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
import config
from additional_text import Additional

game_not_finished = True


def quit_game():
    global game_not_finished
    game_not_finished = False
    additional.additional_end()


screen = Screen()
screen.setup(width=config.SCREEN_WIDTH, height=config.SCREEN_HEIGHT)
screen.bgcolor(config.SCREEN_COLOR)
screen.title(config.SCREEN_TITLE)
screen.tracer(0)

right_paddle = Paddle(config.STARTING_POS_RIGHT, config.PADDLE1_COLOR)
left_paddle = Paddle(config.STARTING_POS_LEFT, config.PADDLE2_COLOR)
pong_ball = Ball()
score_l = Score(config.LEFT_SCORE)
score_r = Score(config.RIGHT_SCORE)
additional = Additional()
screen.update()

screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(quit_game, "q")

while game_not_finished:

    if pong_ball.ycor() > (config.SCREEN_HEIGHT / 2) - 10 or pong_ball.ycor() < - (config.SCREEN_HEIGHT / 2) + 10:
        pong_ball.collision_with_wall()

    if ((pong_ball.xcor() > config.STARTING_POS_RIGHT[0] - 25 and pong_ball.distance(right_paddle) < 50) or
            (pong_ball.xcor() < config.STARTING_POS_LEFT[0] + 25 and pong_ball.distance(left_paddle) < 50)):
        pong_ball.collision_with_paddle()

    if pong_ball.xcor() > config.SCREEN_WIDTH / 2:
        pong_ball.reset_pos()
        score_l.score += 1
        score_l.score_refresh()

    if pong_ball.xcor() < -config.SCREEN_WIDTH / 2:
        pong_ball.reset_pos()
        score_r.score += 1
        score_r.score_refresh()

    pong_ball.ball_move()
    time.sleep(0.01)
    screen.update()


screen.exitonclick()
