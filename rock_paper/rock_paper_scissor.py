import random


def main():
    times = input("write no of times you wanna play! ").strip()
    if times.isdigit():
        times = int(times)
        count = 0
        while count < times:
            print(rps())
            count += 1
    else:
        print("Print nos. only")


def rps():
    user = input("Respond (R) for rock, (S) for scissor, (P) for paper: ").upper().strip()
    opponent_list = ["R", "P", "S"]
    opp = random.choice(opponent_list)
    dict_game = {
        "R": "Rock",
        "S": "Scissor",
        "P": "Paper"
    }
    if user == "R" or user == "S" or user == "P":
        print(f"You: {dict_game[user]} and Opponent: {dict_game[opp]}")
        if user == opp:
            return "Match tied"
        elif (
            (user == "R" and opp == "S")
            or (user == "P" and opp == "R")
            or (user == "S" and opp == "S")
        ):
            return "You Win"
        elif (
                (user == "R" and opp == "P")
                or (user == "P" and opp == "S")
                or (user == "S" and opp == "R")
        ):
            return "You lost"
    else:
        return "invalid character"


if __name__ == "__main__":
    main()

