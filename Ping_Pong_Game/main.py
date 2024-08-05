from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('green')
screen.title('Ping Pong')

def draw_field():
    field = Turtle()
    field.hideturtle()
    field.penup()
    field.color('white')
    field.speed('fastest')
    
    # Draw outer border
    field.goto(-390, 290)
    field.pendown()
    for _ in range(2):
        field.forward(780)
        field.right(90)
        field.forward(580)
        field.right(90)
    field.penup()
    
    # Draw center line
    field.goto(0, 290)
    field.setheading(270)
    field.pendown()
    for _ in range(29):
        field.forward(10)
        field.penup()
        field.forward(10)
        field.pendown()

draw_field()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Scoreboard()



obstacle = Ball()
# my_player.color('red')
# my_player.shape('square')
# my_player.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=None)
is_game_on = True


def exits():
    global is_game_on
    is_game_on = False


screen.listen()
screen.onkey(r_paddle.go_up, key='Up')
screen.onkey(r_paddle.go_down, key='Down')
screen.onkey(l_paddle.go_up, key='w')
screen.onkey(l_paddle.go_down, key='s')
screen.onkey(exits , key='q')

# or instead of screen.tracer(1)
# while is_game_on is true update screen

while is_game_on:
    time.sleep(obstacle.move_speed)
    screen.update()
    obstacle.move()
    # detect collision
    if obstacle.ycor() > 280 or obstacle.ycor() < -280:
        obstacle.bounce_y()

    # detect collision with paddle
    if (obstacle.distance(r_paddle) < 50 and obstacle.xcor() > 320 or obstacle.distance(l_paddle) < 50
            and obstacle.xcor() < -320):
        obstacle.bounce_x()
    if obstacle.xcor() > 380:
        obstacle.reset_position()
        score.l_point()

    if obstacle.xcor() < -380:
        obstacle.reset_position()
        score.r_point()

screen.exitonclick()
