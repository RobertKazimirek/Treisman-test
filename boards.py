import instruction
from psychopy import visual, core, event


def show_board(window, text, to_continue="\n\n\nAby kontynuować, naciśnij dowolny przycisk.", size=None):
    msg = visual.TextBox2(window, text=text+to_continue, font="Open Sans", alignment="centre", letterHeight=size)
    msg.draw()
    window.flip()

    keyboard = event.waitKeys()


def show_instruction(window):
    show_board(window, instruction.INSTRUCTION, size=0.02)


def show_error_board(window):
    msg = visual.TextBox2(window, text="BŁĄD!", letterHeight=0.2, bold=True, font="Open Sans", alignment="centre")
    msg.draw()
    window.flip()
    core.wait(0.5)
    event.clearEvents()


def show_training_board(window):
    show_board(window, "Za chwilę rozpoczniesz krótką sesję treningową.", size=0.025)


def show_second_training_board(window, score):
    show_board(window, f"Zakończono 1. sesję treningową."
                       f"\n\nLiczba poprawnych odpowiedzi: {score} na 6 możliwych."
                       f"\n\nPrzed Tobą 2. sesja treningowa.", size=0.025)


def show_training_end_board(window, score):
    show_board(window, f"Zakończono sesję treningową."
                       f"\n\nLiczba poprawnych odpowiedzi: {score} na 6 możliwych."
                       f"\n\n Przed Tobą pierwsza sesja eksperymentalna.", size=0.025)


def show_score_board(window, session_number, score):
    if session_number == 3:
        return

    show_board(window, f"Zakończono {session_number}. sesję eksperymentalną."
                       f"\n\nLiczba poprawnych odpowiedzi: {score} na 60 możliwych."
                       f"\n\nPrzed Tobą {session_number+1}. sesja eksperymentalna.", size=0.025)


def show_final_board(window, score):
    show_board(window, f"Zakończono ostatnią sesję eksperymentalną."
                       f"\n\nLiczba poprawnych odpowiedzi: {score} na 60 możliwych."
                       f"\n\nBardzo dziękujemy za wzięcie udziału w badaniu!",
               "\n\n\nW celu wyjścia, naciśnij dowolne miejsce na ekranie.", size=0.025)
