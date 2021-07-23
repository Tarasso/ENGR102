# Braedon Lindsey, Scottie Taylor, Lauren Corradino, and Kyle Mrosko
# ENGR 102 - 212
# Lab 11 Act 2 B
# An aggie does not lie, cheat or steal, or tolerate those who do.

filename = input("Enter the name of the file to be read: ") + ".csv"

userfile = open(filename, "r")

data = []
for line in userfile:
    data.append(line[:-1].split(" "))

userfile.close()

x = [float(data[i][0]) for i in range(len(data))]
y = [float(data[i][1]) for i in range(len(data))]


def interpolate(x_values, y_values):
    values = {}

    for i in range(len(x_values)):
        values[x_values[i]] = y_values[i]

    sorted_values = sorted(values)

    while True:
        n = int(input("Enter the number of items in the list (enter 0 to stop): "))
        x_list, y_list = [], []

        if n <= 0:
            break

        for i in range(n):
            x_list.append(float(input("Enter an x value: ")))

        for i in range(n):
            x_value = x_list[i]
            if x_value < sorted_values[0]:
                x1 = sorted_values[0]
                x2 = sorted_values[1]
                y1 = values[x1]
                y2 = values[x2]
                slope = (y2 - y1) / (x2 - x1)
                ans = y1 + slope * (x_value - x1)
                y_list.append(ans)
            elif x_value > sorted_values[-1]:
                x1 = sorted_values[-2]
                x2 = sorted_values[-1]
                y1 = values[x1]
                y2 = values[x2]
                slope = (y2 - y1) / (x2 - x1)
                ans = y1 + slope * (x_value - x1)
                y_list.append(ans)
            else:
                for i in range(len(sorted_values)):
                    if x_value >= sorted_values[i]:
                        x1 = sorted_values[i]
                        x2 = sorted_values[i + 1]
                        y1 = values[x1]
                        y2 = values[x2]
                        slope = (y2 - y1) / (x2 - x1)
                        ans = y1 + slope * (x_value - x1)
                        y_list.append(ans)
                        break

        print(f"x = {x_list}\ny = {y_list}")


interpolate(x, y)