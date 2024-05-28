from dataclasses import dataclass

@dataclass
class Trial:
    trialNumber: int
    numb_of_disp_obj: int
    is_positive: bool
    is_conjunction: bool
    reactionTime: float
    is_correct: bool
    #shape/color while dysjunction might be added but it will recquire more changes


@dataclass
class Session:
    sessionNumber: int
    number_of_correct: int
    trials: list[Trial]


@dataclass
class DataContainer:
    sessions: list[Session]
