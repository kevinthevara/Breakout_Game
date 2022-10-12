from turtle import Screen, Turtle
from ball import Ball
import time
r1 = 250
r2 = 150
r3 = 50
screen = Screen()
losses = 0
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)



ball=Ball()
paddle= Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=7, stretch_len=1)
paddle.penup()
paddle.goto(0, -240)
#0,-240
paddle.right(90)
ball.goto(0,-100)



scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.game_score = 0


lst = []
x = -315
y = 250
for n in range(10):
    if n != 0:
        x = -315
        y -= 30
    for b in range(7):
        t = Turtle("square")
        t.color("white")
        t.shapesize(stretch_wid=4.5, stretch_len=1)
        t.penup()
        t.right(90)
        t.goto(x, y)
        lst.append(t)
        x += 100


def go_right():
    new_x = paddle.xcor() + 20
    paddle.goto(new_x, paddle.ycor())


def go_left():
    new_x = paddle.xcor() - 20
    paddle.goto(new_x, paddle.ycor())


screen.listen()
screen.onkeypress(go_right, "Right")


screen.onkeypress(go_left, "Left")
game = True
while game:
    time.sleep(ball.move_speed)

    ball.move()
    screen.update()

    if ball.ycor() > 300:
        ball.bounce_y()
    elif ball.xcor() > 380:
        ball.bounce_x()
    elif ball.xcor() < -380:
        ball.bounce_x()
# ----------------------------------------------------------
#Bouncing Against Paddle
    if ball.distance(paddle) < 73 and ball.ycor() < -217:
        ball.bounce_y()


#Bouncing Against Blocks
    for item in lst:
        if ball.distance(item) < 40:
            ball.bounce_y()
            lst.remove(item)
            item.hideturtle()
            scoreboard.game_score+=5


#Win or Lose
    if ball.ycor() < -225:
        ball.reset_position()
        losses+=1
        if losses == 3:
            print(f"You Lost! Your Score: {scoreboard.game_score}")

            screen.clear()
            screen.bgcolor("black")
            scoreboard.score_text = scoreboard.write(scoreboard.game_score, align="center",font=("Courier", 80, 'normal'))
            game = False
    if len(lst) == 0:
        screen.clear()
        screen.bgcolor("black")
        scoreboard.score_text = scoreboard.write(scoreboard.game_score, align="center", font=("Courier", 80, 'normal'))
        print("You WON! Your Score: 500")
        game= False

screen.exitonclick()
