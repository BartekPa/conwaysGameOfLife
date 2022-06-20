import PySimpleGUI as sg
import time

global temp


def creating_UI():
    default_time = 10
    temp = 1

    file_list_column = [
        [sg.Text("Would you like to choose basic parameters of the game? (Y/N)")],
        [sg.Text("Is it square? (Y/N)", visible=False, key='-TEXT SQUARE-')],
        [sg.Text("What is the square width? (3-7)", visible=False, key='-TEXT WIDTH SQ-')],
        [sg.Text("What is the rectangle width? (3-7)", visible=False, key='-TEXT WIDTH RT-')],
        [sg.Text("What is the rectangle height? (3-7)", visible=False, key='-TEXT HEIGHT RT-')],
        [sg.Text("The default parameters will be loaded in {:d} seconds".format(default_time),
                 key='-TEXT TIME TO DEFAULT-'), ],


    ]

    user_answer = [
        [sg.InputText(size=(2, 2), key="-MAIN ANSWER-")],
        [sg.InputText(size=(2, 2), visible=False, key="-SQUARE ANSWER-")],
        [sg.InputText(size=(5, 2), visible=False, key="-WIDTH SQ ANSWER-")],
        [sg.InputText(size=(5, 2), visible=False, key="-WIDTH RT ANSWER-")],
        [sg.InputText(size=(5, 2), visible=False, key="-HEIGHT RT ANSWER-")],

    ]

    user_confirmation = [
        [sg.Button("OK", key='-BUTTON MAIN-')],
        [sg.Button("OK", visible=False, key='-BUTTON SQ-')],
        [],
        [],
        [sg.Button("OK", visible=False, key='-BUTTON SIZE-')],

    ]

    # ----- Full layout -----

    layout = [

        [
            sg.Column(file_list_column),
            sg.Column(user_answer),
            sg.Column(user_confirmation)
        ]

    ]

    window = sg.Window("Conway\'s Game", layout, size=(600,200), text_justification = 'r')

    tic = time.time()
    default = True
    while True:

        event, values = window.read(timeout=10)

        toc = time.time()

        if toc - tic >= default_time and default:
            default = True
            print('Default parameters was loaded...')
            break
        elif toc - tic >= 1 * temp and default:
            window['-TEXT TIME TO DEFAULT-'].update(
                "The default parameters will be loaded in {:d} seconds".format(int(default_time) - temp))
            temp = temp + 1

        if event == "-BUTTON MAIN-":
            print('Button readed!', str(window['-MAIN ANSWER-'].get()))
            if str(window['-MAIN ANSWER-'].get()) == ('Y' or 'y'):
                default = False
                #window['-TEXT TIME TO DEFAULT-'].update('User configuration!')
                window['-TEXT TIME TO DEFAULT-'].update(visible=False)
                window['-TEXT SQUARE-'].update(visible=True)
                window['-SQUARE ANSWER-'].update(visible=True)
                window['-BUTTON SQ-'].update(visible=True)
                window["-BUTTON MAIN-"].update(visible=False)
                window['-MAIN ANSWER-'].update(disabled=True)
            elif str(window['-MAIN ANSWER-'].get()) == ('N' or 'n'):
                default = True
                break
            else:
                sg.Popup('Wrong input data! Please answer (Y/N)')
                window['-MAIN ANSWER-'].update('')
                tic = toc
                temp = 1

        if event == '-BUTTON SQ-':
            if str(window["-SQUARE ANSWER-"].get()) == ('Y' or 'y'):
                window['-TEXT WIDTH SQ-'].update(visible=True)
                window['-WIDTH SQ ANSWER-'].update(visible=True)
                window['-BUTTON SIZE-'].update(visible=True)
                window['-BUTTON SQ-'].update(visible=False)
                window["-SQUARE ANSWER-"].update(disabled=True)
            elif str(window["-SQUARE ANSWER-"].get()) == ('N' or 'n'):
                window['-TEXT WIDTH RT-'].update(visible=True)
                window['-TEXT HEIGHT RT-'].update(visible=True)
                window["-WIDTH RT ANSWER-"].update(visible=True)
                window["-HEIGHT RT ANSWER-"].update(visible=True)
                window['-BUTTON SIZE-'].update(visible=True)
                window['-BUTTON SQ-'].update(visible=False)
                window["-SQUARE ANSWER-"].update(disabled=True)
            else:
                sg.Popup('Wrong input data! Please answer (Y/N)')
                window["-SQUARE ANSWER-"].update('')

        if event == '-BUTTON SIZE-':
            print('BUTTON SQ ANSWER:', window["-WIDTH SQ ANSWER-"].get())
            print('BUTTON RT ANSWER:', window["-WIDTH RT ANSWER-"].get())
            print('Type:', window["-WIDTH SQ ANSWER-"].get().isdigit())
            if window["-WIDTH SQ ANSWER-"].get().isdigit() and 2 < int(window["-WIDTH SQ ANSWER-"].get()) < 8:
                width = int(window['-WIDTH SQ ANSWER-'].get())
                height = width
                break
            elif int(window["-WIDTH RT ANSWER-"].get().isdigit() and window["-HEIGHT RT ANSWER-"].get().isdigit()) and 2 < int(window["-WIDTH RT ANSWER-"].get()) < 8 and 2 < int(window["-HEIGHT RT ANSWER-"].get()) < 8:
                width = int(window['-WIDTH RT ANSWER-'].get())
                height = int(window['-HEIGHT RT ANSWER-'].get())
                break
            else:
                sg.Popup('Wrong input data! Please answer in range 3-7')
                window['-WIDTH RT ANSWER-'].update('')
                window['-HEIGHT RT ANSWER-'].update('')
                window['-WIDTH SQ ANSWER-'].update('')


        if event == "Exit" or event == sg.WIN_CLOSED:
            exit()

    if default:
        width = 4
        height = width

    window.close()
    return width, height
