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
t.speed('fastest')
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
    print('While in move to start begin! currentPositionVertical ={}, currentPositionHorizontal = {}'.format(
        currentPositionVertical, currentPositionHorizontal))
    while currentPositionVertical != 0 or currentPositionHorizontal != 0:
        print('While in move to start begin!')
        if currentPositionVertical > 0:
            move_down(squareLength)
        elif currentPositionVertical < 0:
            move_up(squareLength)

        if currentPositionHorizontal > 0:
            move_left(squareLength)
        elif currentPositionHorizontal < 0:
            move_right(squareLength)


def draw_grid(width, hight, playField, square_len):
    t.clear()
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

        for i in range(width):
            move_left(square_len)

    move_to_start(square_len)


draw_grid(width, hight, playField, square_len)

def calculate_new_field(playField1):
    playField_new = playField1.copy()
    full_grids = 0
    case = [0, 0, 0, 0]
    for squares_wd in range(width):
        for squares_hg in range(hight):

            if squares_wd == 0:
                case[0] = 1
            else:
                case[0] = 0

            if squares_wd == width - 1:
                case[1] = 1
            else:
                case[1] = 0

            if squares_hg == 0:
                case[2] = 1
            else:
                case[2] = 0

            if squares_hg == hight - 1:
                case[3] = 1
            else:
                case[3] = 0

            print('Case = {}, Hight = {}, Width = {}'.format(case, squares_wd, squares_hg))
            if case == [1, 0, 0, 0]:
                full_grids = full_grids + playField1[squares_wd, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd, squares_hg + 1]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg + 1]

            elif case == [1, 0, 1, 0]:
                full_grids = full_grids + playField1[squares_wd, squares_hg + 1]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg + 1]

            elif case == [0, 1, 0, 0]:
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg]
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg + 1]
                full_grids = full_grids + playField1[squares_wd, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd, squares_hg + 1]

            elif case == [0, 1, 1, 0]:
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg]
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg + 1]
                full_grids = full_grids + playField1[squares_wd, squares_hg + 1]

            elif case == [0, 1, 0, 1]:
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg]
                full_grids = full_grids + playField1[squares_wd, squares_hg - 1]

            elif case == [0, 0, 1, 0]:
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg]
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg + 1]
                full_grids = full_grids + playField1[squares_wd, squares_hg + 1]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg + 1]

            elif case == [0, 0, 0, 1]:
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg]
                full_grids = full_grids + playField1[squares_wd, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg]

            elif case == [1, 0, 0, 1]:
                full_grids = full_grids + playField1[squares_wd, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg]

            else:
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg]
                full_grids = full_grids + playField1[squares_wd - 1, squares_hg + 1]
                full_grids = full_grids + playField1[squares_wd, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd, squares_hg + 1]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg - 1]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg]
                full_grids = full_grids + playField1[squares_wd + 1, squares_hg + 1]

            print('full_grids ={}, playField[squares_wd, squares_hg] = {}'.format(full_grids,
                                                                                  playField1[squares_wd, squares_hg]))
            if playField1[squares_wd, squares_hg] == 1 and (full_grids == 2 or full_grids == 3):
                playField_new[squares_wd, squares_hg] = 1
                full_grids = 0
            elif playField1[squares_wd, squares_hg] == 0 and full_grids == 3:
                playField_new[squares_wd, squares_hg] = 1
                full_grids = 0
            else:
                playField_new[squares_wd, squares_hg] = 0
                full_grids = 0


    return playField_new

playField_new2 = calculate_new_field(playField)
draw_grid(width, hight, playField, square_len)

while True:
    playField_new3 = playField_new2.copy()
    print('Playfield_new2:\n', playField_new2)
    playField_new2 = calculate_new_field(playField_new2)
    print('Playfield_new3:\n', playField_new3)

    if not playField_new2.any() or np.array_equiv(playField_new2,playField_new3):
        break
    draw_grid(width, hight, playField_new2, square_len)


a = input('Press double Enter to close the program!')
