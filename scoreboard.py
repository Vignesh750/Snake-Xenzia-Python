import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
            print(self.highscore)
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.speed("fastest")
        self.goto(x=0, y=270)
        self.write(arg=f"Score : {self.point} , Highscore : {self.highscore}", move=False, align="center",
                   font=('Arial', 20, 'normal'))

    def increase_point(self):
        self.point += 1
        self.clear()
        self.write(arg=f"Score : {self.point} , Highscore : {self.highscore}",
                   move=False, align="center", font=('Arial', 20, 'normal'))

    def set_highscore(self):
        if self.point > self.highscore:
            self.highscore = self.point
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.clear()
        self.point = 0
        self.write(arg=f"Score : {self.point} , Highscore : {self.highscore}", move=False, align="center",
                   font=('Arial', 20, 'normal'))

    def game_over(self):
        self.hideturtle()
        self.goto(x=0, y=0)
        self.pencolor("red")
        self.speed("fastest")
        self.write(arg=f"Game Over \n Score : {self.point}", move=False, align="center", font=('Arial', 20, 'normal'))
