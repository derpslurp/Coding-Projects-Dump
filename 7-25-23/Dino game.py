import turtle
import random

wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(height=600,width=900)
wn.tracer(0)
wn.title("PARKOUR GAME")
#gameover text
go = turtle.Turtle()
go.color('black')
go.hideturtle()
go.penup()
go.goto(0,0)

scoreText = turtle.Turtle()
scoreText.color('black')
scoreText.hideturtle()
scoreText.penup()
scoreText.goto(0,250)
scoreText.write('SCORE: 0', align='center', font=('Courier', 30, 'normal'))

player = turtle.Turtle()
player.color("black")
player.penup()
player.goto(-350,20)
player.shape("square")
player.dy = 0
player.dx = 0

floor = turtle.Turtle()
floor.color("black",'white')
floor.speed(0)
floor.shape("square")
floor.penup()
floor.goto(0,-280)
floor.shapesize(stretch_len=1000,stretch_wid=2)

s = turtle.clone()
s.color("black")
s.left(90)
s.speed(0)
s.shape("triangle")
s.penup()
s.goto(500,-250)
s.shapesize(stretch_wid=1.5,stretch_len=1.5)
s.dx = -0.5
s.hideturtle()

m = turtle.clone()
m.color("black")
m.left(90)
m.speed(0)
m.shape("triangle")
m.penup()
m.goto(800,-243)
m.shapesize(stretch_wid=3,stretch_len=3)
m.dx = -0.4
m.hideturtle()

fs = turtle.clone()
fs.color("black")
fs.speed(0)
fs.left(180)
fs.shape("triangle")
fs.penup()
fs.goto(500,-150)
fs.shapesize(stretch_wid=1.5,stretch_len=1.5)
fs.dx = -0.5
fs.hideturtle()

gravity = -0.01

score = 0

player.goto(-350, -250)

def jump():
    if player.state == "ready":
        player.dy = 1.7
        player.state = "jumping"

wn.listen()
wn.onkeypress(jump,"space")

def tap(x,y):
    print(x,y)
wn.onscreenclick(tap)

st = random.randint(30,60)
st1 = random.randint(40,70)
st2 = random.randint(60,80)

while True:
    wn.update()

    p = s
    p.dx = -0.5
    p.showturtle()

    d = fs
    d.dx = -0.35
    d.showturtle()

    c = m
    c.dx = -0.4
    c.showturtle()

    player.dy += gravity

    y = player.ycor()
    y += player.dy
    player.sety(y)
    player.state = "jumping"

    sx = p.xcor()
    sx += p.dx
    p.setx(sx)

    sx1 = d.xcor()
    sx1 += d.dx
    d.setx(sx1)

    sx2 = c.xcor()
    sx2 += c.dx
    c.setx(sx2)

    if player.ycor() < -250:
        player.sety(-250)
        player.setheading(0)
        player.state = "ready"

    if player.state == 'jumping':
        player.right(0.5)
        wn.update()

    st -= 0.01
    st1 -= 0.01
    st2 -= 0.01

    if st <= 0:
        p = s
        p.goto(500,-250)
        p.dx = -0.5
        p.showturtle()
        st = random.randint(30, 60)
    if st1 <= 0:
        d = fs
        d.goto(500,-150)
        d.dx = -0.35
        d.showturtle()
        st1 = random.randint(40, 70)

    if st2 <= 0:
        c = m
        c.goto(800,-243)
        c.dx = -0.4
        c.showturtle()
        st2 = random.randint(60, 80)

    if player.ycor() < -220 and player.xcor() < p.xcor() + 1 and player.xcor() > p.xcor() - 1:
        wn.clear()
        go.write('GAME OVER', align='center', font=('Courier', 50, 'normal'))
        scoreText.goto(0,-100)
        scoreText.write('SCORE: {}'.format(score), align='center', font=('Courier', 30, 'normal'))
    elif player.ycor() > -220 and player.xcor() < p.xcor() + 1 and player.xcor() > p.xcor() - 1:
        score += 1
        scoreText.clear()
        scoreText.write('SCORE: {}'.format(score), align='center', font=('Courier', 30, 'normal'))

    if player.ycor() > -240 and player.xcor() < d.xcor() + 1 and player.xcor() > d.xcor() - 1:
        wn.clear()
        go.write('GAME OVER', align='center', font=('Courier', 50, 'normal'))
        scoreText.goto(0,-100)
        scoreText.write('SCORE: {}'.format(score), align='center', font=('Courier', 30, 'normal'))
    elif player.ycor() < -220 and player.xcor() < d.xcor() + 1 and player.xcor() > d.xcor() - 1:
        score += 1
        scoreText.clear()
        scoreText.write('SCORE: {}'.format(score), align='center', font=('Courier', 30, 'normal'))

    if player.ycor() < -240 and player.xcor() < c.xcor() + 5 and player.xcor() > c.xcor() - 5:
        wn.clear()
        go.write('GAME OVER', align='center', font=('Courier', 50, 'normal'))
        scoreText.goto(0,-100)
        scoreText.write('SCORE: {}'.format(score), align='center', font=('Courier', 30, 'normal'))
    elif player.ycor() > -240 and player.xcor() < c.xcor() + 5 and player.xcor() > c.xcor() - 5:
        score += 2
        scoreText.clear()
        scoreText.write('SCORE: {}'.format(score), align='center', font=('Courier', 30, 'normal'))