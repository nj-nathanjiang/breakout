import turtle as t


class Wall(t.Turtle):

    def __init__(self, x, y, color):
        super().__init__()
        self.color("black")
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.penup()
        self.goto(x, y)
        self.color(color)
        self.bouncable = True

    def destroy(self):
        self.color("black")
        self.bouncable = False
