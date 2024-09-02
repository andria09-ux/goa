from turtle import *


#we want to paint a house

#step 1: square
begin_fill()
speed(10)
width(7)
color("yellow")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
begin_fill()
forward(70)
color("brown")
left(90)
forward(120)     #hight of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows
begin_fill()
color("light blue")
penup()
goto(0,120)
pendown()
left(120)
forward(65)
left(90)
forward(70)
left(90)
forward(65)
end_fill()


penup()
goto(200, 120)
pendown()
begin_fill()
forward(65)
right(90)
forward(70)
right(90)
forward(65)
end_fill()

color("blue")
penup()
goto(32, 120)
pendown()
left(90)
forward(70)
penup()
goto(0, 155)
pendown()
right(90)
forward(65)

penup()
goto(165, 120)
pendown()
left(90)
forward(70)
penup()
goto(200, 155)
pendown()
left(90)
forward(65)

exitonclick()