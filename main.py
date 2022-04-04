import random as rd
import turtle
import numpy as np

width = 4
hight = width
fieldSize = hight * width

playFieldWidth = np.array([])
playField = np.array([])
print(playField.size)

for ht in range(hight):
    for wd in range(width):
        playFieldWidth = np.append(playFieldWidth, [1 if rd.random() > 0.5 else 0])
        print('Play Width:', playFieldWidth)

    # playField =np.append(playField, playFieldWidth, 0)
    if playField.size == 0:
        playField = playFieldWidth
    else:
        playField = np.vstack([playField, playFieldWidth])
    print('Play Field:', playField)
    playFieldWidth = np.array([])

square_len = 50
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-square_len * hight / 2, square_len * width / 2)
t.pendown()
t.speed(0)
currentPositionHorizontal = 0
currentPositionVertical = 0


def draw_square(squareLength):
    for i in range(0, 4):
        t.forward(squareLength)
        t.right(90)


def move_right(squareLength):
    global currentPositionHorizontal
    t.forward(squareLength)
    currentPositionHorizontal = currentPositionHorizontal + 1


def move_left(squareLength):
    global currentPositionHorizontal
    t.right(180)
    t.forward(squareLength)
    t.right(180)
    currentPositionHorizontal = currentPositionHorizontal - 1


def move_down(squareLength):
    global currentPositionVertical
    t.right(90)
    t.forward(squareLength)
    t.left(90)
    currentPositionVertical = currentPositionVertical - 1


def move_up(squareLength):
    global currentPositionVertical
    t.left(90)
    t.forward(squareLength)
    t.right(90)
    currentPositionVertical = currentPositionVertical + 1


def move_to_start(squareLength):
    global currentPositionVertical
    global currentPositionHorizontal

    while currentPositionVertical == 0 and currentPositionHorizontal == 0:
        if currentPositionVertical > 0:
            move_down(squareLength)
        elif currentPositionVertical < 0:
            move_up(squareLength)

        if currentPositionHorizontal > 0:
            move_left(squareLength)
        elif currentPositionHorizontal < 0:
            move_right(squareLength)


for squares_wd in range(width):
    for squares_hg in range(hight):
        if playField[squares_wd, squares_hg] == 1:
            t.begin_fill()
            t.fillcolor('black')
            draw_square(square_len)
            t.end_fill()
        else:
            draw_square(square_len)

        move_right(square_len)
    move_down(square_len)
    for i in range(hight):
        move_left(square_len)

move_to_start(square_len)
print("playfield size", len(playField))
calculated_square = 0
while calculated_square <= hight * width:
    if calculated_square%width ==0:

    calculated_square = calculated_square + 1
playField_new = playField.copy()
a = input('Press double Enter to close the program!')
