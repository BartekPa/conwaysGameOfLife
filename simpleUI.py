import PySimpleGUI as sg
import time


def creating_UI():
    file_list_column = [

        [sg.Text("Would you like to choose basic parameters of the game? (Y/N)")],
        [sg.Text("Is it square? (Y/N)", visible=False, key='-TEXT SQUARE-')],
        [sg.Text("What is the square width? (3-7)", visible=False, key='-TEXT WIDTH SQ-')],
        [sg.Text("What is the rectangle width? (3-7)", visible=False, key='-TEXT WIDTH RT-')],
        [sg.Text("What is the rectangle height? (3-7)", visible=False, key='-TEXT HEIGHT RT-')],

    ]

    user_answer = [

        [sg.InputText(size=(2, 2), key="-MAIN ANSWER-")],
        [sg.InputText(size=(2, 2), visible=False, key="-SQUARE ANSWER-")],
        [sg.InputText(size=(5, 2), visible=False, key="-WIDTH SQ ANSWER-")],
        [sg.InputText(size=(5, 2), visible=False, key="-WIDTH RT ANSWER-")],
        [sg.InputText(size=(5, 2), visible=False, key="-HEIGHT RT ANSWER-")],

    ]

    user_confirmation = [
        [sg.Button("OK", key='-BUTTON-')],
        [sg.Button("OK", visible=False, key='-BUTTON SQ-')],
        [],
        [],
        [sg.Button("OK", visible=False, key='-BUTTON RT-')],
    ]

    # ----- Full layout -----

    layout = [

        [
            sg.Column(file_list_column),
            sg.Column(user_answer),
            sg.Column(user_confirmation)
        ]

    ]

    window = sg.Window("Conway\'s Game", layout)

    tic = time.time()
    default = True
    while True:

        event, values = window.read(timeout=10)
        toc = time.time()

        if toc - tic >= 5 and default:
            default = True
            print('Default parameters was loaded...')
            break

        if event == "-BUTTON-":
            print('Button readed!', str(window['-MAIN ANSWER-'].get()))
            if str(window['-MAIN ANSWER-'].get()) == 'Y' or 'y':
                default = False
                window['-TEXT SQUARE-'].update(visible=True)
                window['-SQUARE ANSWER-'].update(visible=True)
                window['-BUTTON SQ-'].update(visible=True)
                window["-BUTTON-"].update(visible=False)

        if event == '-BUTTON SQ-':
            if str(window["-SQUARE ANSWER-"].get()) == 'Y' or 'y':
                window['-TEXT WIDTH SQ-'].update(visible=True)
                window['-WIDTH SQ ANSWER-'].update(visible=True)
                window['-BUTTON RT-'].update(visible=True)
                window['-BUTTON SQ-'].update(visible=False)
            elif str(window["-SQUARE ANSWER-"].get()) == 'N' or 'n':
                window['-TEXT WIDTH RT-'].update(visible=True)
                window['-TEXT HEIGHT RT-'].update(visible=True)
                window["-WIDTH RT ANSWER-"].update(visible=True)
                window["-HEIGHT RT ANSWER-"].update(visible=True)
                window['-BUTTON RT-'].update(visible=True)
                window['-BUTTON SQ-'].update(visible=False)

        if event == '-BUTTON RT-':
            print('BUTTON SQ ANSWER:', window["-WIDTH SQ ANSWER-"].get())
            if 2 < int(window["-WIDTH SQ ANSWER-"].get()) < 8:
                width = int(window['-WIDTH SQ ANSWER-'].get())
                height = width
                break
            elif 2 < int(window["-WIDTH RT ANSWER-"].get()) < 8 and 2 < int(window["-HEIGHT RT ANSWER-"].get()) < 8:
                width = window['-WIDTH RT ANSWER-'].get()
                height = window['-HEIGHT RT ANSWER-'].get()
                break

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    if default:
        width = 4
        height = width

    window.close()
    return width, height
