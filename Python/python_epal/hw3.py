import turtle as t
t.shape ("turtle")
t.bgcolor("black")
t.color("red")
t.pensize(4)
t.speed(10)
t.hideturtle()
t.penup()

def square():
               t.pendown()
               t.forward(15)
               t.left(90)
               t.forward(15)
               t.left(90)
               t.forward(15)
               t.left(90)
               t.forward(15)
               t.left(90)
               t.penup()
               
t.goto(0,0)
square()

t.goto(50,50)
square()

t.goto(150,150)
square()

t.goto(200,200)
square()

t.exitonclick
