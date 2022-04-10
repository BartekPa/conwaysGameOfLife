from threading import Thread
import PySimpleGUI as sg
import time
import os.path

counting = '0'


def start_timer():
    for i in range(5):
        counting = '{} left until default paraemters will start'.format(5 - i)
        time.sleep(1)




file_list_column = [

    [
        sg.Text("Woud you like to choose basic paraemters of the game? (Y/N)"),

    ],

    [
        sg.Text(counting)
    ],

]

image_viewer_column = [

    [sg.InputText(size=(5, 1), key="-ANSWER-")],

]

user_confirmation = [
    [sg.Button("OK")],
]

# ----- Full layout -----

layout = [

    [

        sg.Column(file_list_column),

        sg.Column(image_viewer_column),

        sg.Column(user_confirmation)

    ]

]

window = sg.Window("Image Viewer", layout)

# Run the Event Loop

while True:

    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # Folder name was filled in, make a list of files in the folder

window.close()

threadlist = []

threadlist.append(Thread(target=user_answer))
threadlist.append(Thread(target=start_timer))

for t in threadlist:
    t.start()

for t in threadlist:
    t.join()
