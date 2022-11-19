import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.color("red")
        self.goto_new_position()

    def goto_new_position(self):
        self.goto(random.randint(-260, 260), random.randint(-260, 260))



