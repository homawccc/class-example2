import turtle

wn=turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.delay(0)
#paddle-a
pada = turtle.Turtle()
pada.speed(0)
pada.shape("square")
pada.color("black")
pada.shapesize(5, 1)
pada.penup()
pada.goto(-380, 0)
pada.color("white")
#paddle-b
padb = turtle.Turtle()
padb.speed(0)
padb.shape("square")
padb.color("black")
padb.shapesize(5, 1)
padb.penup()
padb.goto(370, 0)
padb.color("white")
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=.1
ball.dy=-.1
#function - move paddles
def pada_up():
    y = pada.ycor()
    y+=20
    pada.sety(y)
def pada_down():
    y = pada.ycor()
    y+=-20
    pada.sety(y)
def padb_up():
    y = padb.ycor()
    y+=20
    padb.sety(y)
def padb_down():
    y = padb.ycor()
    y+=-20
    padb.sety(y)
#keyboard binding
wn.listen()
wn.onkeypress(pada_up, "w")
wn.onkeypress(pada_down, "s")
wn.onkeypress(padb_up, "Up")
wn.onkeypress(padb_down, "Down")

while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border checking (top)
    if ball.ycor() > 290:
        ball.dy = -(ball.dy)
    if ball.ycor() < -290:
        ball.dy = -(ball.dy)
    #through sides
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = -(ball.dx)
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = -(ball.dx)
    #collision with paddles
    if (ball.xcor() < -350 and ball.xcor() >-370) and (ball.ycor() < pada.ycor() + 40 and ball.ycor() > pada.ycor() - 40):
        ball.dx = -(ball.dx)
    if (ball.xcor() > 350 and ball.xcor() < 370) and (ball.ycor() < padb.ycor() + 40 and ball.ycor() > padb.ycor() - 40):
        ball.dx = -(ball.dx)

wn.mainloop()



