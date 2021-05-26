import turtle as t
import paddle as p
import ball as b
import wall as w
import scoreboard as s
import time

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.title("Breakout")

paddle = p.Paddle()

screen.listen()
screen.onkeypress(fun=paddle.go_right, key="d")
screen.onkeypress(fun=paddle.go_left, key="a")
screen.onkeypress(fun=paddle.go_right, key="Right")
screen.onkeypress(fun=paddle.go_left, key="Left")

walls = []

x_initial = -240
y_initial = 375
for n in range(8):
    walls.append(w.Wall(x=x_initial, y=y_initial, color="red"))
    if (n + 1) % 8 == 0:
        x_initial = -240
        y_initial -= 25
    else:
        x_initial += 65

for n in range(8):
    walls.append(w.Wall(x=x_initial, y=y_initial, color="orange"))
    if (n + 1) % 8 == 0:
        x_initial = -240
        y_initial -= 25
    else:
        x_initial += 65

for n in range(8):
    walls.append(w.Wall(x=x_initial, y=y_initial, color="yellow"))
    if (n + 1) % 8 == 0:
        x_initial = -240
        y_initial -= 25
    else:
        x_initial += 65

ball = b.Ball()
ball.reset_ball()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.distance(paddle.paddle) < 90 and ball.ycor() < -325:
        ball.y_bounce()
    elif ball.ycor() < -325:
        ball.reset_ball()

    for wall in walls:
        if wall.distance(ball) < 50 and wall.ycor() + 10 > ball.ycor() > wall.ycor() - 10 and wall.bouncable:
            wall.destroy()
            ball.x_bounce()

screen.exitonclick()
