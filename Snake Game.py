
from turtle import Screen
from turtle import Turtle
import time

import random
POSITION1 = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    segments = []

    def createSnake(self, POSITION, colour):
        for pos in POSITION:
            tx = Turtle()
            tx.penup()
            tx.shape("square")
            tx.color(colour)
            tx.goto(pos)
            self.segments.append(tx)

    def moveSnake(self):
        for segnum in range(len(self.segments)-1, 0, -1):
            self.segments[segnum].goto(
                self.segments[segnum-1].xcor(), self.segments[segnum-1].ycor())
        self.segments[0].forward(20)

    def leftMove(self):
        self.segments[0].setheading(180)

    def rightMove(self):
        self.segments[0].setheading(0)

    def upMove(self):
        self.segments[0].setheading(90)

    def downMove(self):
        self.segments[0].setheading(270)

    def extend(self):
        tx = Turtle()
        tx.penup()
        tx.shape("square")
        tx.color("green")
        tx.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(tx)


scr = Screen()
scr.screensize(600, 600)
scr.bgcolor("black")
scr.tracer(0)

snake_obj1 = Snake()
snake_obj1.createSnake(POSITION1, "green")

f = Turtle()
f.color("green")
f.penup()
f.shape("circle")
f.goto(random.randint(-280, 280), random.randint(-280, 280))


score = 0
sb = Turtle()
sb.hideturtle()

sb.goto(0, 250)
sb.color("green")
sb.clear()
sb.write(score, move=False, align="center", font=("Arial", 20, "normal"))


scr.update()
scr.listen()

scr.onkey(snake_obj1.leftMove, "Left")
scr.onkey(snake_obj1.rightMove, "Right")
scr.onkey(snake_obj1.upMove, "Up")
scr.onkey(snake_obj1.downMove, "Down")

n = 1

while n == 1:
    snake_obj1.moveSnake()
    scr.update()
    time.sleep(0.3)
    if (snake_obj1.segments[0].distance(f) < 20):
        snake_obj1.extend()

        f.goto(random.randint(-280, 280), random.randint(-280, 280))
        score = score+1
        sb.clear()
        sb.write(score, move=False, align="center",
                 font=("Arial", 20, "normal"))
    if (snake_obj1.segments[0].xcor() > 290 or snake_obj1.segments[0].xcor() < -290 or snake_obj1.segments[0].ycor() > 290 or snake_obj1.segments[0].ycor() < -290):
        sb.penup()
        sb.goto(0, 0)
        sb.pendown()
        sb.write("Game over", move=False, align="center",
                 font=("Arial", 30, "normal"))
        n = 0


scr.exitonclick()
