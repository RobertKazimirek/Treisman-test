import boards
import DataContainer

from psychopy import visual, event, clock, core

import random

GREEN = (50, 200, 100)
BROWN = (150, 100, 75)
BLUE = (60, 100, 220)


def get_positions(numb_of_disp_obj):
    if numb_of_disp_obj == 4:
        return [14, 15, 20, 21]
    elif numb_of_disp_obj == 16:
        return [7, 8, 9, 10, 13, 14, 15, 16, 19, 20, 21, 22, 25, 26, 27, 28]
    else:
        return list(range(36))


def specify_target(is_conjunction):
    if is_conjunction:
        target = (GREEN, 'T')

    else:
        target_variation = random.randint(0, 3)
        if target_variation == 0:
            target = (BLUE, 'X')
        elif target_variation == 1:
            target = (BLUE, 'T')
        elif target_variation == 2:
            target = (GREEN, 'S')
        else:
            target = (BROWN, 'S')

    return target


def create_elements(numb_of_disp_obj, is_positive, is_conjunction):
    distr_variation = [i // (numb_of_disp_obj // 2) for i in range(numb_of_disp_obj)]
    random.shuffle(distr_variation)

    elements = []
    for element_idx in range(numb_of_disp_obj):
        if distr_variation[element_idx]:
            elements.append((GREEN, 'X'))
        else:
            elements.append((BROWN, 'T'))

    target = specify_target(is_conjunction)

    if is_positive:
        positive_position = random.randint(0, numb_of_disp_obj-1)
        elements[positive_position] = target

    return elements, target


def display_target(window, target):
    visual.TextBox2(window, text=target[1], font="Open Sans", pos=(0, 0), alignment='centre', letterHeight=0.14, bold=True, color=target[0], colorSpace='rgb255').draw()

    window.flip()


def display_elements(window, elements, numb_of_disp_obj):
    positions = get_positions(numb_of_disp_obj)

    for element_idx, element in enumerate(elements):
        y = (positions[element_idx] // 6 - 2.5) * 0.16
        x = (positions[element_idx] % 6 - 2.5) * 0.16

        visual.TextBox2(window, text=element[1], font="Open Sans", pos=(x, y), alignment='centre', letterHeight=0.14, bold=True, color=element[0], colorSpace='rgb255').draw()

    window.flip()


def run_trial(trial_number, window, numb_of_disp_obj, is_positive, is_conjunction):
    elements, target = create_elements(numb_of_disp_obj, is_positive, is_conjunction)

    display_target(window, target)
    core.wait(0.5)
    display_elements(window, elements, numb_of_disp_obj)

    trial_data = DataContainer.Trial(trial_number, numb_of_disp_obj, is_positive, is_conjunction, 0, False)
    m_clock = clock.Clock()

    keyboard = event.waitKeys(keyList=['z', 'm'])

    is_correct = True if ((keyboard[0] == 'z' and not is_positive) or (keyboard[0] == 'm' and is_positive)) else False
    reaction_time = m_clock.getTime()

    trial_data.is_correct = is_correct
    trial_data.reactionTime = reaction_time

    return trial_data
