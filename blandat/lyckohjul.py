import random
import turtle

t = turtle.Turtle()
t.speed(100)

t.left(90)

colour = (random.randint(0,3))
if colour == 0:
 color = ("red")
elif colour == 3:
 color = ("blue")
elif colour == 2:
 color = ("green")
elif colour == 1:
 color = ("yellow")

t.penup()
t.setposition(0, 0)
t.pendown()
for x in range(250):
 t.pencolor(color)
 t.forward(200)
 t.left(0.36)
 t.penup()
 t.setposition(0, 0)
 t.pendown()

colour = (random.randint(0,3))
if colour == 0:
  color = ("red")
elif colour == 3:
  color = ("blue")
elif colour == 2:
  color = ("green")
elif colour == 1:
  color = ("yellow")

for x in range(250):
 t.pencolor(color)
 t.forward(200)
 t.left(0.36)
 t.penup()
 t.setposition(0, 0)
 t.pendown()

colour = (random.randint(0,3))
if colour == 0:
 color = ("red")
elif colour == 3:
 color = ("blue")
elif colour == 2:
 color = ("green")
elif colour == 1:
 color = ("yellow")

for x in range(250):
 t.pencolor(color)
 t.forward(200)
 t.left(0.36)
 t.penup()
 t.setposition(0, 0)
 t.pendown()

colour = (random.randint(0,3))
if colour == 0:
 color = ("red")
elif colour == 3:
 color = ("blue")
elif colour == 2:
 color = ("green")
elif colour == 1:
 color = ("yellow")
for x in range(250):
 t.pencolor(color)
 t.forward(200)
 t.left(0.36)
 t.penup()
 t.setposition(0, 0)
 t.pendown()

t.pencolor("black")
t.penup()
t.right(90)
t.setposition(50, 100)
t.pendown()
t.right(75)
t.forward(75)
t.left(120)
t.forward(40)
t.right(75)
t.forward(40)
t.left(120)
t.forward(75)

t.penup()
t.setposition(-100, -50)
t.pendown()
t.right(165)
t.forward(75)
t.left(120)
t.forward(40)
t.right(75)
t.forward(40)
t.left(120)
t.forward(75)

t.penup()
t.setposition(50, -50)
t.pendown()
t.right(180)
t.forward(75)
t.left(90)
t.forward(40)

t.penup()
t.setposition(-100, 100)
t.pendown()
t.right(90)
t.forward(75)
t.left(90)
t.forward(40)

input()