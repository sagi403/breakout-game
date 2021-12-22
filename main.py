from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from tkinter import messagebox

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle(pos=(0, -250))
ball = Ball(pos=(0, -220))
blocks = Blocks()

screen.listen()
screen.onkey(paddle.paddle_left, "Left")
screen.onkey(paddle.paddle_right, "Right")

blocks.generate_blocks()

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with paddle
    if ball.ycor() < -230 and ball.distance(paddle) < 50:
        ball.bounce_paddle()

    # Detect collision with side wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_side_wall()

    # Detect collision with upper wall
    if ball.ycor() > 280:
        ball.bounce_upper_wall()

    # Reset out of bounds
    if ball.ycor() < -300:
        is_game_on = False
        messagebox.showinfo(title="Game Over", message=f"Your score is: {blocks.score}")

    # Detect collision with block
    for block in blocks.all_blocks:
        if block.distance((ball.xcor(), ball.ycor())) < 40:
            if (ball.ycor() + 30 <= block.ycor() <= ball.ycor() + 40) or \
                    ball.ycor() - 40 <= block.ycor() <= ball.ycor() - 30:
                ball.bounce_base_block()
            if (ball.xcor() + 30 <= block.xcor() <= ball.xcor() + 40) or \
                    ball.xcor() - 40 <= block.xcor() <= ball.xcor() - 30:
                ball.bounce_side_block()
            blocks.delete_block(block)

screen.exitonclick()
