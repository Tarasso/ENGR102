x = 1
y = 10
z = 0

z += x
print(z)

x += 1
z += x
print(z)

z = 0
x = 1
y += x
z += y
print(z)

y = 10
z = 0
x += 1
y += x
y += x
y *= 2
z += y
print(z)

z = 0
x = 1
y = 10
x += y
y *= 10
y += x
y += x
x = 1
z += x
z += y
print(z)

y = 10
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
z = 0
z += y
print(z)

z = 0
y = 10
x = 1
z += x
x += 1
y *= x
z += y
x += 1
y = 10
x = y
y *= x
x = 1
x += 1
x += 1
y *= x
z += y
y = 10
x = 1
x = y
y *= x
y *= x
x = 1
x += 1
x += 1
x += 1
y *= x
z += y
print(z)