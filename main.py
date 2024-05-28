import dataclasses
import boards
import DataContainer
import session

from psychopy import visual, core
import json
import datetime
import random


def save_results(data_container):
    data = dataclasses.asdict(data_container)
    json_data = json.dumps(data)

    with open(f"Results\\treisman_{str(datetime.datetime.now()).replace(' ', '_').replace(':', '-')[:-7]}.json", "x") as file:
        file.write(json_data)


def main():
    window = visual.Window(units="height", fullscr=True, monitor=None, color=(26, 26, 26), colorSpace='rgb255')
    data_container = DataContainer.DataContainer([])

    boards.show_instruction(window)

    boards.show_training_board(window)
    result = session.run_session(0, window, True, True).number_of_correct
    boards.show_second_training_board(window, result)
    result = session.run_session(0, window, True, False).number_of_correct
    boards.show_training_end_board(window, result)

    is_conjunction_list = [1, 0, 0, 1] if random.randint(0, 1) else [0, 1, 1, 0]
    for index, is_conjunction in enumerate(is_conjunction_list):
        session_data = session.run_session(index+1, window, False, is_conjunction)
        data_container.sessions.append(session_data)
        boards.show_score_board(window, index+1, session_data.number_of_correct)
    boards.show_final_board(window, data_container.sessions[-1].number_of_correct)

    save_results(data_container)

    window.close()
    core.quit()


if __name__ == '__main__':
    main()

