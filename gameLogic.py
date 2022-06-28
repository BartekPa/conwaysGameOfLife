def calculate_new_field(play_field, width, height):
    play_field_new = play_field.copy()
    full_grids = 0
    case = [0, 0, 0, 0]

    '''
    square
    
    |1|2|2|3|
    |4|5|5|6|
    |4|5|5|6|
    |7|8|8|9|
    
    case[0] =1 - no square on the left
    case[1] =1 - no square on the right
    case[2] =1 - no square above
    case[3] =1 - no square below 
    
    
    '''

    for squares_wd in range(width):
        for squares_hg in range(height):

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

            if squares_hg == height - 1:
                case[3] = 1
            else:
                case[3] = 0

            if case[0] == 0:
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg]
            if case[1] == 0:
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg]
            if case[2] == 0:
                full_grids = full_grids + play_field[squares_wd, squares_hg - 1]
            if case[3] == 0:
                full_grids = full_grids + play_field[squares_wd, squares_hg + 1]
            if case[1] == 0 and case[3] == 0:
                full_grids = full_grids + play_field[squares_wd+1, squares_hg + 1]
            if case[0] == 0 and case[2] == 0:
                full_grids = full_grids + play_field[squares_wd-1, squares_hg - 1]
            if case[1] == 0 and case[2] == 0:
                full_grids = full_grids + play_field[squares_wd+1, squares_hg - 1]
            if case[0] == 0 and case[3] == 0:
                full_grids = full_grids + play_field[squares_wd-1, squares_hg + 1]



            if play_field[squares_wd, squares_hg] == 1 and (full_grids == 2 or full_grids == 3):
                play_field_new[squares_wd, squares_hg] = 1
                full_grids = 0
            elif play_field[squares_wd, squares_hg] == 0 and full_grids == 3:
                play_field_new[squares_wd, squares_hg] = 1
                full_grids = 0
            else:
                play_field_new[squares_wd, squares_hg] = 0
                full_grids = 0

    print('Output from function logic:',play_field_new)
    return play_field_new


''' def calculate_new_field(play_field, width, height):
    play_field_new = play_field.copy()
    full_grids = 0
    case = [0, 0, 0, 0]
    for squares_wd in range(width):
        for squares_hg in range(height):

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

            if squares_hg == height - 1:
                case[3] = 1
            else:
                case[3] = 0

            if case == [1, 0, 0, 0]:
                full_grids = full_grids + play_field[squares_wd, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd, squares_hg + 1]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg + 1]

            elif case == [1, 0, 1, 0]:
                full_grids = full_grids + play_field[squares_wd, squares_hg + 1]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg + 1]

            elif case == [0, 1, 0, 0]:
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg]
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg + 1]
                full_grids = full_grids + play_field[squares_wd, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd, squares_hg + 1]

            elif case == [0, 1, 1, 0]:
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg]
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg + 1]
                full_grids = full_grids + play_field[squares_wd, squares_hg + 1]

            elif case == [0, 1, 0, 1]:
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg]
                full_grids = full_grids + play_field[squares_wd, squares_hg - 1]

            elif case == [0, 0, 1, 0]:
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg]
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg + 1]
                full_grids = full_grids + play_field[squares_wd, squares_hg + 1]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg + 1]

            elif case == [0, 0, 0, 1]:
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg]
                full_grids = full_grids + play_field[squares_wd, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg]

            elif case == [1, 0, 0, 1]:
                full_grids = full_grids + play_field[squares_wd, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg]

            else:
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg]
                full_grids = full_grids + play_field[squares_wd - 1, squares_hg + 1]
                full_grids = full_grids + play_field[squares_wd, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd, squares_hg + 1]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg - 1]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg]
                full_grids = full_grids + play_field[squares_wd + 1, squares_hg + 1]

            if play_field[squares_wd, squares_hg] == 1 and (full_grids == 2 or full_grids == 3):
                play_field_new[squares_wd, squares_hg] = 1
                full_grids = 0
            elif play_field[squares_wd, squares_hg] == 0 and full_grids == 3:
                play_field_new[squares_wd, squares_hg] = 1
                full_grids = 0
            else:
                play_field_new[squares_wd, squares_hg] = 0
                full_grids = 0

    print('Output from function logic:',play_field_new)
    return play_field_new'''
