# Braedon Lindsey, Lauren Corradino, Scottie Taylor, Kyle Mrosko
# ENGR 102-212
# Lab 10 Assignment 1
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

#As a team, we
#have gone through all required sections of the tutorial, and each team member

import numpy as np
import matplotlib

# Create four matrices
a = np.arange(-3,9).reshape(3,4)
b = np.arange(-4,4).reshape(4,2)
c = np.arange(-7,-1).reshape(2,3)
d = np.arange(-2,1).reshape(3,1)
print("a =",a,"b =",b,"c =",c,"d =",d,sep="\n")

# Preform operations
e = (a @ b) @ c
print("e (a times b times c) =\n",e)
e_transpose = e.transpose()
print("e transpose =\n",e_transpose)
x = np.linalg.solve(e,d)
print("Ex = D, x =\n",x)