import turtle as t


class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        if -285 >= self.xcor() or self.xcor() >= 275:
            self.x_bounce()
        elif self.ycor() >= 375:
            self.y_bounce()
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto((x, y))

    def x_bounce(self):
        self.x_move = -self.x_move
        self.move_speed *= 0.2

    def y_bounce(self):
        self.y_move = -self.y_move
        self.move_speed *= 0.2

    def reset_ball(self):
        self.color("black")
        self.move_speed = 0.1
        self.goto(0, 0)
        self.color("white")
