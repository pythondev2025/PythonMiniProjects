import _curses
import curses
from curses import wrapper
import time


def main(stdscr):
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the test. press any key to try gain and \"esc\" to cancel.")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Test.")
    stdscr.addstr("\nPress any key to continue.")
    stdscr.refresh()
    stdscr.getkey()


def wpm_test(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)

    target_text = "hello there! you have to type this out in order to pass the wpm test."
    current_text = []
    correct_words = ''
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        stdscr.clear()
        stdscr.addstr(target_text)
        stdscr.addstr(1, 0, f"WPM: {wpm}")

        correct_text = []
        for i, char in enumerate(current_text):
            if target_text[i] == char:
                stdscr.addstr(0, i, char, curses.color_pair(1))
                correct_text.append(char)
                correct_words = "".join(correct_text)
                correct_words = correct_words.split(" ")
            else:
                if char == " ":
                    stdscr.addstr(0, i, char, curses.color_pair(4))
                else:
                    stdscr.addstr(0, i, char, curses.color_pair(2))
        stdscr.refresh()

        if len(current_text) == len(target_text):
            stdscr.nodelay(False)
            break
        if len(current_text) >= 1:
            elapsed_time = time.time() - start_time
            if len(correct_words) >= 1:
                wpm = round((len(correct_words) * 60) / elapsed_time)

        try:
            key = stdscr.getkey()
        except _curses.error:
            continue

        if ord(key) == 27:
            break
        if (
            key in ("KEY_BACKSPACE", "\b", "\x7f")
            and len(current_text) > 0
        ):
            current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


if __name__ == "__main__":
    wrapper(main)
