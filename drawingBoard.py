import random as rd
import turtle
import numpy as np

global t, square_len
square_len= 50
currentPositionHorizontal = 0
currentPositionVertical = 0

def init_draw(height,width):
    global t, square_len

    playFieldWidth = np.array([])
    playField = np.array([])

    for ht in range(width):
        for wd in range(height):
            playFieldWidth = np.append(playFieldWidth, [1 if rd.random() > 0.5 else 0])
        if playField.size == 0:
            playField = playFieldWidth
        else:
            playField = np.vstack([playField, playFieldWidth])
        playFieldWidth = np.array([])

    t = turtle.Turtle()
    t.hideturtle()
    t.speed('fastest')
    t.penup()
    t.goto(-square_len * width / 2, square_len * height / 2)
    t.pendown()
    return(playField)




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

    while currentPositionVertical != 0 or currentPositionHorizontal != 0:

        if currentPositionVertical > 0:
            move_down(squareLength)
        elif currentPositionVertical < 0:
            move_up(squareLength)

        if currentPositionHorizontal > 0:
            move_left(squareLength)
        elif currentPositionHorizontal < 0:
            move_right(squareLength)


def draw_grid(width, height, playField, square_len):
    t.clear()
    print('Draw_grid parameters:', width, height)
    for squares_hg in range(height):
        print('squares_hg: ', squares_hg)
        for squares_wd in range(width):
            print('squares_wd: ',squares_wd)
            if playField[squares_wd, squares_hg] == 1:
                t.begin_fill()
                t.fillcolor('black')
                draw_square(square_len)
                t.end_fill()
            else:
                draw_square(square_len)

            move_right(square_len)
        move_down(square_len)

        for i in range(width):
            move_left(square_len)

    move_to_start(square_len)

