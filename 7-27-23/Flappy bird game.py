import turtle
import random

list = []

for i in range(220,300):
    list.append(-i)
wn = turtle.Screen()
wn.bgcolor("cyan")
wn.setup(height=500,width=600)
wn.tracer(0)
wn.title("FLAPPY BIRD GAME")

go = turtle.Turtle()
go.color('black')
go.hideturtle()
go.penup()
go.goto(0,0)

scoreText = turtle.Turtle()
scoreText.color('black')
scoreText.hideturtle()
scoreText.penup()
scoreText.goto(-180,200)
scoreText.write('SCORE: 0', align='center', font=('Courier', 30, 'normal'))

player = turtle.Turtle()
player.color("yellow")
player.penup()
player.goto(-200,0)
player.shape("square")
player.dy = 0
player.dx = 0

tp = turtle.clone()
tp.color('black','lime')
tp.penup()
tp.goto(200,350)
tp.shape('square')
tp.shapesize(stretch_wid=20,stretch_len=1.5)
tp.dx = -0.2
tp.hideturtle()

lp = turtle.clone()
lp.color('black','lime')
lp.penup()
lp.goto(200,-200)
lp.shape('square')
lp.shapesize(stretch_wid=20,stretch_len=1.5)
lp.dx = -0.2
lp.hideturtle()

gravity = -0.0005

score = 0

def jump():
    player.dy = 0.3

wn.listen()
wn.onkeypress(jump,"space")

t = 40

while True:
    wn.update()

    a = tp
    a.dx = -0.2
    a.showturtle()

    b = lp
    b.dx = -0.2
    b.showturtle()

    player.dy += gravity

    y = player.ycor()
    y += player.dy
    player.sety(y)

    sx = a.xcor()
    sx += a.dx
    a.setx(sx)

    sx1 = b.xcor()
    sx1 += b.dx
    b.setx(sx1)

    player.right(0.2)

    t -= 0.01

    if t <= 0:
        a = tp
        a.goto(300, random.randint(220,300))
        a.dx = -0.2
        a.showturtle()

        b = lp
        b.goto(300, random.choice(list))
        b.dx = -0.2
        b.showturtle()

        t = 40

    if player.ycor() < -230:
        wn.clear()
        go.write('GAME OVER', align='center', font=('Courier', 50, 'normal'))

    if player.ycor() > a.ycor() - 200 and player.xcor() < a.xcor() + 1 and player.xcor() > a.xcor() - 1 or player.ycor() < b.ycor() + 200 and player.xcor() < b.xcor() + 1 and player.xcor() > b.xcor() - 1:
        wn.clear()
        go.write('GAME OVER', align='center', font=('Courier', 50, 'normal'))
        scoreText.goto(0, -50)
        scoreText.clear()
        scoreText.write('SCORE: {}'.format(score), align='center', font=('Courier', 30, 'normal'))
    elif player.ycor() < a.ycor() - 200 and player.xcor() < a.xcor() + 1 and player.xcor() > a.xcor() - 1 or player.ycor() > b.ycor() + 200 and player.xcor() < b.xcor() + 1 and player.xcor() > b.xcor() - 1:
        score += 1
        scoreText.clear()
        scoreText.write('SCORE: {}'.format(score), align='center', font=('Courier', 30, 'normal'))





