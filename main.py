from drawingBoard import *
from gameLogic import *
from simpleUI import *


[width, height] = creating_UI()
playField = init_draw(height, width)
draw_grid(width, height, playField, square_len)

while True:

    playField_new = calculate_new_field(playField, width, height)

    if np.array_equiv(playField, playField_new):
        print("Comparing Done! The same arrays!")
        break

    draw_grid(width, height, playField_new, square_len)
    playField = playField_new.copy()

a = input('Press double Enter to close the program!')
