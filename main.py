import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong by Avi Singh aka Darkster Twilight")
wn.bgcolor("black")
wn.setup(width=800,height=600) # 800 and 600 are in pixels
wn.tracer(0) # force stop the auto screen updation, screen updated manually,
# increase the game performance

# Score
score_a = 0
score_b = 0

# paddel A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation (max)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)# stretch by 5 times
paddle_a.penup() # by default turtle draw lines but by this it won't
paddle_a.goto(-350, 0)
# paddel b
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of animation (max)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)# stretch by 5 times
paddle_b.penup() # by default turtle draw lines but by this it won't
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation (max)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1,stretch_len=1)# stretch by 5 times
ball.penup() # by default turtle draw lines but by this it won't
ball.goto(0, 0)
ball.dx = 0.2 # hit and try this no.
ball.dy = 0.2#  hit and try this no.

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 18, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor() # returns the y cordinate
    if y<250 :
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # returns the y cordinate
    if y > -250:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # returns the y cordinate
    if y<250 :
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # returns the y cordinate
    if y > -250:
        y -= 20
        paddle_b.sety(y)


# keybord binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    # top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    # botton border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    #  Right Border
    if ball.xcor() > 390: # ball goes off from right side
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 18, "normal"))
    # Left Border
    if ball.xcor() < -390: # ball goes off from left side
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

    # Paddle and ball collision
    # Right Paddle collision
    if ( 340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    # Left paddle collision
    if ( -350 < ball.xcor() < -340) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)