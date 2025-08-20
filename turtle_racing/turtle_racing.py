import turtle
import random
import time


WIDTH, HEIGHT = 750, 600
COLOR = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]


def main():
    no_of_racers = get_racers()
    random.shuffle(COLOR)
    colors = COLOR[:no_of_racers]
    setting_screen()
    print(race(colors))
    time.sleep(7)


def get_racers():
    while True:
        racers = input("Enter the no. of racers (2-10): ").strip()
        if racers.isdigit() and 2 <= int(racers) <= 10:
            return int(racers)


def setting_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")


def racers_motion(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing, -HEIGHT // 2 + 30)
        turtles.append(racer)
    return turtles


def race(colors):
    turtles = racers_motion(colors)
    while True:
        for racer in turtles:
            racer.forward(random.randint(1,25))
            x, y = racer.pos()
            if y >= HEIGHT // 2:
                return f"{colors[turtles.index(racer)].title()} Turtle wins."


if __name__ == "__main__":
    main()
