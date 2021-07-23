# Kyle Mrosko
# ENGR 102 - 212
# Lab12b
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

import turtle as tt
from math import *

def line():
    """Draws a regular tally line"""
    tt.left(90)
    tt.down()
    tt.forward(50)
    tt.up()
    tt.right(90)
    tt.forward(10)
    tt.right(90)
    tt.forward(50)
    tt.left(90)

def diag():
    """Draws a diagonal line"""
    tt.left(90)
    tt.forward(50)
    tt.left(135)
    tt.down()
    tt.forward(50*sqrt(2))
    tt.up()
    tt.left(135)
    tt.forward(60)

def moveDown():
    """Moves the turtle down to the next row of tallys"""
    tt.right(90)
    tt.forward(60)
    tt.right(90)
    tt.forward(250)
    tt.right(180)


num = int(input("Enter a number:"))
lines = 0
tt.up()
tt.speed(0)
while(lines < num):
    lines += 1
    if lines % 5 == 0:
        diag()
        if lines % 25 == 0:
            moveDown()
    else:
        line()

input()