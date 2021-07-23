# Braedon Lindsey, Kyle Mrosko, Lauren Corradino, and Scottie Taylor
# ENGR 102 - 212
# Lab12 Activity 1
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

import matplotlib.pyplot as plt


# function = x ** 2


def calc_area(x, delta_x):
    height = x ** 2
    area = height * delta_x
    return area


def user_input():
    x_min = input("Enter the min x value: ")
    x_max = input("Enter the max x value: ")
    return (float(x_min), float(x_max))


def left_integral(rectangles, boundaries):
    x_min, x_max = boundaries
    delta_x = (x_max - x_min) / rectangles
    total = 0
    for i in range(rectangles):
        total += calc_area(x_min + i*delta_x, delta_x)
    return total


def right_integral(rectangles, boundaries):
    x_min, x_max = boundaries
    delta_x = (x_max - x_min) / rectangles
    total = 0
    for i in range(rectangles):
        total += calc_area(x_min + (i+1)*delta_x, delta_x)
    return total


def center_integral(rectangles, boundaries):
    x_min, x_max = boundaries
    delta_x = (x_max - x_min) / rectangles
    total = 0
    for i in range(rectangles):
        total += calc_area(x_min + (i+0.5)*delta_x, delta_x)
    return total


def trap_integral(rectangles, boundaries):
    x_min, x_max = boundaries
    delta_x = (x_max - x_min) / rectangles
    total = 0
    for i in range(rectangles):
        total += delta_x / 2 * ((x_min+i*delta_x)**2 + (x_min+(i+1)*delta_x)**2)
    return total


TOL = 1e-4
rect = 10
iterations = 1
bounds = user_input()
while True:
    if abs(trap_integral(rect, bounds) - trap_integral(rect*2, bounds)) > TOL:
        rect *= 2
        iterations += 1
        continue
    else:
        print("Trapezoidal integral:", trap_integral(rect*2, bounds))
        print("Iterations:", iterations)
        break

rect = 10
iterations = 1
while True:
    if abs(left_integral(rect, bounds) - left_integral(rect*2, bounds)) > TOL:
        rect *= 2
        iterations += 1
        continue
    else:
        print("Left riemann sum integral:", left_integral(rect*2, bounds))
        print("Iterations:", iterations)
        break

rect = 10
iterations = 1
while True:
    if abs(right_integral(rect, bounds) - right_integral(rect*2, bounds)) > TOL:
        rect *= 2
        iterations += 1
        continue
    else:
        print("Right riemann sum integral:", right_integral(rect*2, bounds))
        print("Iterations:", iterations)
        break

rect = 10
iterations = 1
while True:
    if abs(center_integral(rect, bounds) - center_integral(rect*2, bounds)) > TOL:
        rect *= 2
        iterations += 1
        continue
    else:
        print("Center riemann sum integral:", center_integral(rect*2, bounds))
        print("Iterations:", iterations)
        break