import turtle
t = turtle.Pen()
t.shape("turtle")
t.color("orange")
t.pensize(8)

for i in range(12):
    t.forward(100)
    t.backward(100)
    t.left(30)

t.penup()
t.right(90)
t.forward(100)
t.left(90)

t.color("brown")
t.pendown()
t.pensize(15)
t.circle(100)