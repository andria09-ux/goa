# 1
from turtle import *
speed(30)

def triangle(lomi):
    if i % 2 == 0:
        color("blue")
    else:
        color('red')
    begin_fill()
    forward(10)
    left(120)
    forward(10)
    left(120)
    forward(10)
    end_fill()
    left(30)
    penup()
    forward(10)
    pendown()
    left(90)
    

for i in range(10):
    triangle(i)


exitonclick()
# 2
def hello_world(idk):
    print(idk)
zamn = 12
hello_world(zamn)
# 3
def even_or_odd(whatever):
    if whatever % 2 == 0:
        print('even')
    else:
        print("odd")

even_or_odd(23)
#