# Simple Pong in Python3

import turtle

wn=turtle.Screen()
wn.title ("Pond by @ Paul")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx=0.05
ball.dy=0.05

# Functions
def paddle_a_up():
    y=paddle_a.ycor()
    y +=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y -=20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y +=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y -=20
    paddle_b.sety(y)
# Keyboard binding
wn.listen()
wn.onkey(paddle_a_up,"w")
wn.onkey(paddle_a_down,"s")
wn.onkey(paddle_b_up,"Up")
wn.onkey(paddle_b_down,"Down")
# Main game loop
while True:
    wn.update()
    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
    # Paddle ball collisions
    if ball.xcor()>340 and (ball.ycor()< paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *=-1

    if ball.xcor()<-340 and (ball.ycor()< paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx *=-1
