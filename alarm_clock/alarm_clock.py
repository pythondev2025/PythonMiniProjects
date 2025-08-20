from playsound import playsound
import time


def main():
    alarm(107)


def alarm(seconds):
    time_lapsed = 0
    print("\033[2J")
    while time_lapsed < seconds:
        time.sleep(1)
        time_lapsed += 1
        time_left = seconds - time_lapsed
        minutes = time_left // 60
        sec = round(((time_left/60)-minutes)*60)
        # Clear and Return sequences for f string
        # CLEAR = "\033[2J"
        # CLEAR__AND_RETURN = "\033[H"
        print(f"\033[H{minutes:02}:{sec:02}")
    return playsound("alarm.mp3")


if __name__ == "__main__":
    main()
