from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(self.pos)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def paddle_right(self):
        self.forward(20)

    def paddle_left(self):
        self.backward(20)
