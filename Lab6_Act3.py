# Braedon Lindsey, Kyle Mrosko, Lauren Corradino, and Scottie Taylor
# Lab6_Act3.py
# An Aggie does not lie, cheat or steal or tolerate those who do

print("This program simulates a game a chess and allows users to move pieces on the board")

# defining the original boardstate
board = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"],
]


# definition of the spaces
# A1 B1 C1 D1 E1 F1 G1 H1
# A2 B2 C2 D2 E2 F2 G2 H2
# A3...
# A4...
# A5...
# A6...
# A7...
# A8 B8 C8 D8 E8 F8 G8 H8

# separates the row and column of the input and stores it as a list
def separate(word):
    return [char for char in word]


# printing the board
for row in range(len(board)):
    for col in range(len(board[0])):
        print(board[row][col], end="")
    print("")

# main game loop
while True:
    print("Enter positions using A-H and 1-8 (eg. A1, G6) enter 0 to stop program")

    start = separate(input("Move from: "))
    if len(start) > 2:
        print("This is an invalid position")
        break
    elif len(start) == 1:
        break
    end = separate(input("Move to: "))
    if len(end) > 2:
        print("This is an invalid position")
        break

    if len(start) == 1:
        if start == 0:
            break

    # Determining the column to start from
    if start[0] == "A":
        start_column = 0
    elif start[0] == "B":
        start_column = 1
    elif start[0] == "C":
        start_column = 2
    elif start[0] == "D":
        start_column = 3
    elif start[0] == "E":
        start_column = 4
    elif start[0] == "F":
        start_column = 5
    elif start[0] == "G":
        start_column = 6
    elif start[0] == "H":
        start_column = 7
    else:
        print("This is not on the board...fool!")
        break

    # Determining the column to end at
    if end[0] == "A":
        end_column = 0
    elif end[0] == "B":
        end_column = 1
    elif end[0] == "C":
        end_column = 2
    elif end[0] == "D":
        end_column = 3
    elif end[0] == "E":
        end_column = 4
    elif end[0] == "F":
        end_column = 5
    elif end[0] == "G":
        end_column = 6
    elif end[0] == "H":
        end_column = 7
    else:
        print("This is not on the board...fool!")
        break

    start_row = int(start[1]) - 1
    end_row = int(end[1]) - 1

    # makes sure location is on the board
    if start_row > 7:
        print("This is not on the board...fool!")
        break
    if end_row > 7:
        print("This is not on the board...fool!")
        break

    # checks and moves the piece
    piece = board[start_row][start_column]
    if piece == ".":
        print("Cannot move from an empty space")
        break
    board[end_row][end_column] = piece
    board[start_row][start_column] = "."

    # prints the board
    for row in range(len(board)):
        for col in range(len(board[0])):
            print(board[row][col], end="")
        print("")
