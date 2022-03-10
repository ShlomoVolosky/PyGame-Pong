#Basic Pong with Basic Programing coding, no OOP
import turtle

score_w = 0
score_y = 0

#game window creation:
win = turtle.Screen()
win.title("Pong Game by Shlomo Volosky")
win.bgcolor("black")
win.setup(width=1300, height=900)
win.tracer(0) #prevents game from updating itself while playing

#Creating Game Basics: Paddle White, Paddle Yellow, Ball Red
#Paddle White
paddle_w = turtle.Turtle()
paddle_w.speed(0) #maximum moving speed
paddle_w.shape("turtle")
paddle_w.shapesize(stretch_len=2, stretch_wid=6)
paddle_w.color("white")
paddle_w.penup()
paddle_w.goto(-610, 0) #starting position


#Paddle Yellow
paddle_y = turtle.Turtle()
paddle_y.speed(0) #maximum moving speed
paddle_y.shape("turtle")
paddle_y.tilt(180)
paddle_y.shapesize(stretch_len=2, stretch_wid=6)
paddle_y.color("yellow")
paddle_y.penup()
paddle_y.goto(600, 0) #starting position


#Ball Red
redball = turtle.Turtle()
redball.speed(0) #maximum moving speed
redball.shape("circle")
redball.color("red")
redball.penup()
redball.goto(0, 0) #starting position
#Moving the ball:
redball.dx = 2
redball.dy = -2

#Recording Hits:
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,430)



#Functions to move the paddles:
def paddle_w_up():
    y = paddle_w.ycor()
    y += 20
    paddle_w.sety(y)

def paddle_w_down():
    y = paddle_w.ycor()
    y -= 20
    paddle_w.sety(y)

def paddle_y_up():
    y = paddle_y.ycor()
    y += 20
    paddle_y.sety(y)

def paddle_y_down():
    y = paddle_y.ycor()
    y -= 20
    paddle_y.sety(y)


#Keyboard biding
win.listen()
win.onkeypress(paddle_w_up, "Up")
win.onkeypress(paddle_w_down, "Down")
win.onkeypress(paddle_y_up, "w")
win.onkeypress(paddle_y_down, "x")



#Main game loop
while True:
    win.update()

    #Move the ball
    redball.setx(redball.xcor() + redball.dx)
    redball.sety(redball.ycor() + redball.dy)

    #Windows Borders
    if redball.ycor() > 440:
        redball.sety(440)
        redball.dy *= -1

    elif redball.xcor() > 620:
        redball.setx(620)
        redball.dx *= -1
        score_y += 1
        pen.clear()
        pen.write(f"Player White: {score_w}, Player Yellow: {score_y}", align="center", font=30)
        

    elif redball.ycor() < -440:
        redball.sety(-440)
        redball.dy *= -1

    elif redball.xcor() < -640:
        redball.setx(-640)
        redball.dx *= -1
        score_w += 1
        pen.clear()
        pen.write(f"Player White: {score_w}, Player Yellow: {score_y}", align="center", font=30)

    #Paddle and ball collisions:
    if (redball.xcor() > 580 and redball.ycor() < paddle_y.ycor() + 40 and redball.ycor() > paddle_y.ycor() - 40):
        redball.setx(580)
        redball.dx *= -1
    if (redball.xcor() < -580 and redball.ycor() > paddle_y.ycor() - 40 and redball.ycor() < paddle_y.ycor() + 40):
        redball.setx(-580)
        redball.dx *= -1

