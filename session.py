import DataContainer
import trial
import random


def run_session(session_number, window, is_training, is_conjunction):
    session_data = DataContainer.Session(session_number, 0, [])

    if is_training:
        trials_list = [(numb_of_disp_obj, i//1) for numb_of_disp_obj in [4, 16, 36] for i in range(2)]
        random.shuffle(trials_list)
    else:
        trials_list = [(numb_of_disp_obj, i//10) for numb_of_disp_obj in [4, 16, 36] for i in range(20)]
        random.shuffle(trials_list)

    for trial_idx, (numb_of_disp_obj, is_positive) in enumerate(trials_list):
        trial_data = trial.run_trial(trial_idx, window, numb_of_disp_obj, is_positive, is_conjunction)
        if trial_data.is_correct: session_data.number_of_correct += 1
        session_data.trials.append(trial_data)

    return session_data
