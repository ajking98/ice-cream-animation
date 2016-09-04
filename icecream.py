'''Ahmed Gedi
Section: A2
GTID: 903197142
I worked on the homework assignment alone, using only this semester's
course materials.'''
import turtle
wn = turtle.Screen()
ice = turtle.Turtle()
wn.bgcolor('lightblue')
ice.pensize(135)
ice.color('peru')
#cone
ice.forward(100)
ice.forward(-200)
ice.right(65)
ice.forward(250)
ice.left(132)
ice.forward(248)
#cream
ice.penup()
ice.color('white')
ice.goto(-30,70)
ice.pendown()
ice.right(65)
ice.pensize(300)
ice.forward(60)
#E
ice.speed(4)
ice.penup()
ice.pensize(10)
ice.goto(-290,-250)
ice.color('black')
ice.left(88)
ice.pendown()
ice.forward(100)
ice.right(90)
ice.forward(40)
ice.penup()
ice.goto(-290,-250)
ice.pendown()
ice.forward(40)
ice.penup()
ice.goto(-290,-200)
ice.pendown()
ice.forward(35)
ice.penup()
#N
ice.goto(-200,-250)
ice.left(90)
ice.pendown()
ice.forward(100)
ice.right(155)
ice.forward(110)
ice.left(155)
ice.forward(100)
ice.penup()
#J
ice.goto(0,-150)
ice.right(90)
ice.pendown()
ice.forward(50)
ice.forward(-100)
ice.goto(0,-150)
ice.goto(0,-225)
ice.right(90)
for x in range(1,35):
    ice.right(5)
    ice.forward(2)

ice.penup()
ice.goto(210,-185)
ice.pendown()
for x in range(1,71):
    ice.left(5)
    ice.forward(4)

#Y
ice.penup()
ice.goto(290,-250)
ice.pendown()
ice.forward(50)
ice.left(30)
ice.forward(50)
ice.forward(-50)
ice.right(60)
ice.forward(50)



