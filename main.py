import turtle
import paddle
import ball
import time

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = paddle.Paddle(paddle_side="right")
l_paddle = paddle.Paddle(paddle_side="left")
ball = ball.Ball()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
