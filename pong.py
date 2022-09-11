import turtle
import os

wind = turtle.Screen()
wind.title = "Pong"
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)


# Score
score_A = 0
score_B = 0



# Paddle A 
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350, 0)

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)

# Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0  Player B: 0", align = "center", font =("Courier", 24, "normal"))



# Functions for Paddle A going up or down
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

#Keyboard Binding for Paddle A up
wind.listen()
wind.onkeypress(paddle_A_up, "w")

#Keyboard binding for Paddle A down

wind.listen()
wind.onkeypress(paddle_A_down, "s")

# Functions for Paddle B going up or down
def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

#Keyboard Binding for Paddle B up
wind.listen()
wind.onkeypress(paddle_B_up, "Up")

#Keyboard binding for Paddle B down

wind.listen()
wind.onkeypress(paddle_B_down, "Down")

#Main game loop
while True:
    wind.update()


    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A:{}  Player B: {}".format(score_A, score_B), align = "center", font =("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A:{}  Player B: {}".format(score_A, score_B), align = "center", font =("Courier", 24, "normal"))


    # Paddle and ball collision
    if (ball.xcor() > 340  and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
       ball.setx(340)
       ball.dx *= -1

    if (ball.xcor() < -340  and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
       ball.setx(-340)
       ball.dx *= -1
     

