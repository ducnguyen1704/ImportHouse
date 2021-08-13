import turtle

t = turtle.Turtle()

# vẽ ông mặt trời
t.left(180)
t.penup() 
t.goto(-600, 350)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(80)
t.end_fill()


t.penup() 
t.goto(-640, 300)
t.pendown()
t.fillcolor("red")
t.begin_fill()

t.pensize(3)
t.circle(8)
t.penup() 
t.goto(-565, 300)
t.pendown()
t.pensize(3)
t.circle(8)
t.end_fill()

t.penup() 
t.goto(-645, 250)
t.pendown()

t.fillcolor("white")
t.begin_fill()
t.left(90)
t.circle(42,180)
t.left(90)
t.forward(85)
t.end_fill()

# tia nắng
t.penup() 
t.goto(-600, 350)
t.pendown()
t.right(90)

a = 40
t.forward(a)
t.penup() 
t.backward(190)
t.pendown()
t.backward(a)

t.penup() 
t.goto(-680, 255)
t.pendown()

t.left(90)
t.forward(a)
t.penup() 
t.backward(190)
t.pendown()
t.backward(a)

t.penup() 
t.goto(-665, 315)
t.pendown()
t.right(45)
t.forward(a)
t.penup() 
t.backward(190)
t.pendown()
t.backward(a)

t.penup() 
t.goto(-540, 320)
t.pendown()
t.right(90)
t.forward(a)
t.penup() 
t.backward(190)
t.pendown()
t.backward(a)

t.penup() 
t.goto(230, 150)
t.pendown()
t.right(135)
t.forward(95)

t.penup() 
t.goto(280, 100)
t.pendown()
t.right(90)
t.forward(97)

t.penup() 
t.goto(-700, -350)
t.pendown()
