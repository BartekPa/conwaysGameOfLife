from drawingBoard import *
from gameLogic import *
import time
from multiprocessing import Process

def user_answer():
    input('Woud you like to use default parameters?')

def start_timer():
    for i in range(5):
        print("{}\n", i)
    time.sleep(1)


processlist = []

processlist.append(Process(target=user_answer))
processlist.append(Process(target=start_timer))



for t in processlist:
    t.start()

'''
'''
draw_grid(width, height, playField, square_len)

while True:

    playField_new = calculate_new_field(playField, height, width)

    if np.array_equiv(playField, playField_new):
        print("Comparing Done! The same arrays!")
        break

    draw_grid(width, height, playField_new, square_len)
    playField = playField_new.copy()

a = input('Press double Enter to close the program!')
