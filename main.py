import snake
import turtle
import time
from food import Food
from scoreboard import Score


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
COLOUR = screen.textinput("Snake colour", "Enter the colour of the snake(pink/green/red/blue/purple/orange/white)")
LEVEL = screen.textinput("Difficulty Level", "Which level would you like to play?(easy/normal/hard)")
SHAPE = screen.textinput("Snake Shape", "Enter the shape of the snake.(circle/square)")
snake = snake.Snake(SHAPE, COLOUR)
snake.create_snake()
food = Food()
score = Score()
if LEVEL == "easy":
    speedlevel = 0.15
elif LEVEL == "normal":
    speedlevel = 0.08
else:
    speedlevel = 0.06
screen.listen()


screen.tracer(0)
game_is_on = True
while game_is_on:
    snake.move_snake()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -280) or (snake.head.ycor() > 270 or snake.head.ycor() < -280):
        score.set_highscore()
        snake.vanish_snake()
        snake.list_of_turtles.clear()
        snake.create_snake()
    elif snake.head.distance(food) < 15:
        score.increase_point()
        food.goto_new_position()
        snake.new_segment()
    for segment in snake.list_of_turtles[1:]:
        if snake.head.distance(segment) < 10:
            score.set_highscore()
            snake.vanish_snake()
            snake.list_of_turtles.clear()
            snake.create_snake()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    screen.update()
    time.sleep(speedlevel)

screen.exitonclick()
