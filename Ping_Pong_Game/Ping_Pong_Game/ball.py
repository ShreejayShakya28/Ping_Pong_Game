from turtle import Turtle,Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.color('white')
        # self.shape('circle')
        screen = Screen()
        screen.addshape("Ping_Pong_Game/ball.gif")
        self.shape("Ping_Pong_Game/ball.gif")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.move_speed = 0.1
        self.bounce_x()