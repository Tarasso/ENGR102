# Braedon Lindsey, Kyle Mrosko, Lauren Corradino, and Scottie Taylor
# ENGR 102 - 212
# Lab12 Activity 1
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

import matplotlib.pyplot as plt


def user_input():
    """Accepts input from the user and separates into a list of coefficients"""
    coeffs = input("Enter a list of coefficients to a polynomial (in the form " +
                   "'1,-2,0,4' for x^3 - 2x^2 + 4): ")
    coeffs = coeffs.split(",")
    coeffs = coeffs[::-1]
    coeffs = [float(i) for i in coeffs]
    return coeffs


def deriv(coeffs):
    new_coeffs = []
    for i in range(len(coeffs)):
        new_coeffs.append(coeffs[i] * i)
    new_coeffs.pop(0)
    return new_coeffs


def evaluate(coeffs, x):
    ans = 0
    for i in range(len(coeffs)):
        ans += coeffs[i] * x ** i
    return ans


def evaluate_list(coeffs, x_list):
    y_list = []
    for i in x_list:
        y_list.append(evaluate(coeffs, i))
    return y_list


c0 = user_input()
c1 = deriv(c0)
c2 = deriv(c1)



x_list = [-5 + 0.01 * i for i in range(1000)]

c0_y_list = evaluate_list(c0, x_list)
c1_y_list = evaluate_list(c1, x_list)
c2_y_list = evaluate_list(c2, x_list)

c0maxIndex = c0_y_list.index(max(c0_y_list))
c0minIndex = c0_y_list.index(min(c0_y_list))

c1maxIndex = c1.index(max(c1))
c1minIndex = c1.index(min(c1))

c2maxIndex = c2.index(max(c2))
c2minIndex = c2.index(min(c2))


plt.plot(x_list, c0_y_list, color="red", label="Polynomial")
x_extrema = [x_list[c0minIndex], x_list[c0maxIndex]]
y_extrema = [c0_y_list[c0minIndex], c0_y_list[c0maxIndex]]
plt.scatter(x_extrema, y_extrema, label="Absolute Max and Min", color="red")
plt.plot(x_list, c1_y_list, color="blue", label="First Derivative")
plt.plot(x_list, c2_y_list, color="green", label="Second Derivative")

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()

title = ""
for i in range(len(c0)):
    if i > 0 and c0[i] > 0:
        title += " + "
        title += f"{c0[i]}*x^{i} "
    elif i > 0 and c0[i] < 0:
        title += "- " + f"{str(c0[i])[1:]}*x^{i} "
    else:
        title += f"{c0[i]} "

title += "and its 1st and 2nd derivatives"

plt.title(title)

plt.show()