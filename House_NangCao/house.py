import turtle
import math

t = turtle.Turtle()
# for background
screen = turtle.Screen()
screen.bgcolor("lavender")

# tạo con rùa.
t.color("blue")
t.shape("turtle")
t.shape("turtle")
t.speed(13)

# móng
t.penup()
t.goto(-300,-350)
t.pendown()
t.fillcolor("MistyRose1")
t.begin_fill()
t.pensize(4)
t.pencolor("black")
for i in range(2):
    t.forward(700)
    t.left(90)
    t.forward(90)
    t.left(90)
t.end_fill()

t.left(90)
t.forward(90)
t.right(90)
t.forward(50)

#Thân
t.fillcolor("DeepSkyBlue1")
t.begin_fill()
t.left(90)
t.forward(200)
t.right(90)
t.backward(50)
t.forward(700)
t.backward(50)
t.right(90)
t.forward(200)
t.right(90)
t.forward(600)
t.end_fill()

#mái
t.fillcolor("NavajoWhite1")
t.begin_fill()
t.penup()
t.goto(-300,-60)
t.pendown()

t.right(120)
t.forward(100)
t.right(60)
t.forward(550)
t.forward(50)
t.right(60)
t.forward(100)
t.right(120)
t.forward(700)
t.end_fill()

t.right(120)
# thanh ngang mái
t.forward(20)
t.right(60)
t.forward(680)

#Đỉnh mái
t.penup()
t.goto(-250,28)
t.pendown()
t.left(90)

# Mái tam giác
t.forward(150)
t.right(45)
t.forward(200)
t.right(90)
t.forward(200)

t.left(45)
t.forward(350)

t.left(90)
t.forward(50)
t.left(90)
t.forward(350)

t.right(45)
t.forward(200)
t.left(90)
t.forward(200)

t.left(45)
t.forward(50)

t.penup()
t.goto(350,178)
t.pendown()
t.forward(152)
# Vòng tròn
t.fillcolor("Moccasin")
t.begin_fill()
t.penup()
t.goto(230,150)
t.pendown()
t.right(90)
t.circle(50)
t.end_fill()

t.penup()
t.goto(-20,280)
t.pendown()

t.right(120)
t.forward(120)
t.right(60)

t.forward(344)
t.right(90)
t.forward(155)

# Cửa sổ trên
t.penup()
t.goto(-190,50)
t.pendown()

t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)

t.penup()
t.goto(-170,50)
t.pendown()

t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)

t.penup()
t.goto(-150,50)
t.pendown()

t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)

t.penup()
t.goto(-130,50)
t.pendown()

t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)

#Thân nhà
t.penup()
t.goto(0,-260)
t.pendown()
t.left(180)
t.forward(200)

t.penup()
t.goto(180,-260)
t.pendown()
t.forward(200)

#Thanh đậm
t.penup()
t.goto(190,-260)
t.pendown()

t.pensize(7)
t.forward(200)

t.penup()
t.goto(-10,-260)
t.pendown()
t.pensize(7)
t.forward(200)

# cửa trái
t.pensize(4)
t.penup()
t.goto(-80,-230)
t.pendown()

for i in range(2):
    t.forward(130)
    t.left(90) 
    t.forward(90)
    t.left(90)

#cửa giữa
t.penup()
t.goto(30,-260)
t.pendown()

for i in range(2):
    t.forward(170)
    t.right(90) 
    t.forward(120)
    t.right(90)
    
t.pensize(8)
t.penup()
t.goto(40,-200)
t.pendown()
t.forward(30)
t.penup()
t.goto(55,-185)
t.pendown()
t.circle(3)

# cửa phải
t.pensize(4)
t.penup()
t.goto(315,-230)
t.pendown()

for i in range(2):
    t.forward(130)
    t.left(90) 
    t.forward(90)
    t.left(90)

# ô cửa con phải
t.penup()
t.goto(295,-215)
t.pendown()
t.fillcolor("White")
t.begin_fill()
for i in range(2):
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.left(90)

t.penup()
t.goto(295,-160)
t.pendown()

for i in range(2):
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()

# ô cửa con trái
t.penup()
t.goto(-100,-215)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for i in range(2):
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.left(90)

t.penup()
t.goto(-100,-160)
t.pendown()

for i in range(2):
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()

# Bậc thang
t.penup()
t.goto(-5,-260)
t.pendown()

t.backward(30)
t.right(90)
t.forward(190)
t.left(90)
t.forward(30)
# Bậc thang
t.penup()
t.goto(-5,-290)
t.pendown()

t.left(90)
t.forward(20)
t.left(90)
t.forward(30)
t.left(90)
t.forward(230)
t.left(90)
t.forward(30)
t.left(90)
t.forward(20)

t.penup()
t.goto(-25,-320)
t.pendown()

t.forward(20)
t.left(90)
t.forward(30)
t.left(90)
t.forward(270)
t.left(90)
t.forward(30)
t.left(90)
t.forward(20)