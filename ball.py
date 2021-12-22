from turtle import Turtle
import random

random_bounce = [-1, 1]


class Ball(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.goto(pos)
        self.move_speed = 0.03

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_side_wall(self):
        self.x_move *= -1

    def bounce_upper_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.y_move *= -1
        self.x_move *= int(random.choice(random_bounce))

    def bounce_base_block(self):
        self.y_move *= -1

    def bounce_side_block(self):
        self.x_move *= -1
