import turtle
import time

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

paddle = turtle.Turtle(shape="square")
paddle.penup()
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.goto(350, 0)


def move_up():
    y_pos = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), y_pos)


def move_down():
    y_pos = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), y_pos)


screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
