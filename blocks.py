from turtle import Turtle

COLORS = ["blue", "green", "red"]


class Blocks:

    def __init__(self):
        self.all_blocks = []
        self.pos_x = -350
        self.pos_y = 120
        self.score = 0

    def generate_blocks(self):
        for n in range(3):
            while self.pos_x < 350:
                new_block = Turtle("square")
                new_block.shapesize(stretch_wid=2, stretch_len=2)
                new_block.penup()
                new_block.goto(self.pos_x, self.pos_y)
                self.pos_x += 60
                new_block.color(COLORS[n])
                self.all_blocks.append(new_block)
            self.pos_x = -350
            self.pos_y += 50

    def delete_block(self, block):
        if block in self.all_blocks:
            if block.color()[0] == "red":
                self.score += 3
            if block.color()[0] == "green":
                self.score += 2
            if block.color()[0] == "blue":
                self.score += 1
            block.reset()
            block.penup()
            block.goto(1000, 1000)




