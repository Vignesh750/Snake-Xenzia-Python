import turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SPEED = "fastest"

class Snake:

    def __init__(self, shape, colour):
        self.list_of_turtles = []
        self.shape = shape
        self.colour = colour
    def create_snake(self):
        for i in range(3):
            new_turtle = turtle.Turtle(shape=self.shape)
            new_turtle.color(self.colour)
            self.list_of_turtles.append(new_turtle)
            new_turtle.penup()
            new_turtle.goto(y=0, x=-20 * i)

        self.head = self.list_of_turtles[0]

    def move_snake(self):
        for turtle_num in range(len(self.list_of_turtles) - 1, 0, -1):
            new_y = self.list_of_turtles[turtle_num - 1].ycor()
            new_x = self.list_of_turtles[turtle_num - 1].xcor()
            self.list_of_turtles[turtle_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def new_segment(self):
        new_turtle = turtle.Turtle(shape=self.shape)
        new_position = self.list_of_turtles[-1].pos()
        new_turtle.goto(new_position)
        new_turtle.color(self.colour)
        new_turtle.speed(SPEED)
        self.list_of_turtles.append(new_turtle)
        new_turtle.penup()

    def vanish_snake(self):
        for seg in self.list_of_turtles:
            seg.goto(1000, 1000)






