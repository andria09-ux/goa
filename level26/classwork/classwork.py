# def ixvis_tolma():
#     print("იხვის ტოლმა ბაჟეში")
# ixvis_tolma()
from turtle import *

speed(10)
color("red")
width(10)

def walk():
    forward(200)
    left(90)
    forward(200)


def fall_back():
    penup()
    goto(0,0)
    pendown()

def do_all():
    walk()
    fall_back()

def idk(raodenoba):

    for i in range(raodenoba):
        do_all()

idk(5)

idk(10)

exitonclick()