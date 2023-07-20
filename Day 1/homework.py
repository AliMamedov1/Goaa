from turtle import *


#we want to paint a house

#step 1: deaw a square
speed(30)
width(7)
color("red")
forward (200)
left(90)

forward (200)
left(90)


forward (200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(115)

penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
penup()
goto(150, 150)
pendown()

color("brown")
begin_fill()
right(150)
forward(25)
left(50)
right(50)
color("Brown")
begin_fill()
right(50)
left(50)
forward(15)
goto(150, 150)
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
penup()
goto(20, 180)
pendown()

color("brown")
begin_fill()
left(90)
forward(33)
left(90)
forward(35)
left(90)
forward(40)
left(90)
forward(40)
left
left(40)











exitonclick()
