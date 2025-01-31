import turtle as t
t.shape ("turtle")
t.bgcolor("black")
t.color("red")
t.pensize(4)
t.speed(10)
t.hideturtle()
t.penup()

def square():
	for x in range(4):
		t.pendown()
		t.forward(15)
		t.left(90)
		
for R in range(0, 51, 50):
		t.goto(R,R)
		square()
		t.penup()

for M in range(150, 201, 50):
		t.goto(M,M)
		square()
		t.penup()
