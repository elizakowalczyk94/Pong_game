import turtle
import paddle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = paddle.Paddle(paddle_side=" right")
l_paddle = paddle.Paddle(paddle_side="left")

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
