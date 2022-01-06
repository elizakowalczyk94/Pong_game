from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, paddle_side):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.paddle_side = paddle_side.lower()
        self.choose_paddle_side(side=paddle_side)

    def choose_paddle_side(self, side):
        if side == "right":
            self.goto(350, 0)
        elif side == "left":
            self.goto(-350, 0)
        else:
            raise ValueError("Argument 'paddle_side' can be 'right' or 'left'.")

    def move_up(self):
        y_pos = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_pos)

    def move_down(self):
        y_pos = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y_pos)
