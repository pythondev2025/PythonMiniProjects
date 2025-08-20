import random


def main():
    d_game()


def d_game():
    players = input("enter no of players (2-4): ")
    if players.isdigit() and 2 <= int(players) <= 4:
        players = int(players)
        score_list = []
        turns_list = []
        for i in range(players):
            print(f"Its turn of Player {i+1}")
            score = 0
            turns = 0
            while True:
                res = input("do you wanna continue: (y) or (n): ").lower()
                if res == "y":
                    value = random.randint(0,6)
                    turns += 1
                    score += value
                    print(f"Turn: {turns}")
                    if value == 0:
                        print(f"You rolled: {value}")
                        print("Your turn ended.")
                        score = 0
                        print(f"Your total scores are {score} in {turns} no. of turns.")
                        break
                    elif score >= 50:
                        print(f"You rolled {value}")
                        print(f"Your total scores are {score} and you completed the game.")
                        break
                    else:
                        print(f"You rolled: {value}")
                        print(f"Your total scores are {score}")
                        print("\n")
                elif res == "n":
                    print("Your turn ended.")
                    print(f"Your total scores are {score} in {turns} no. of turns.")
                    break
                else:
                    print("Invalid character.")
            print("\n\n")
            score_list.append(score)
            turns_list.append(turns)
        winner = 0
        for i in range(players):
            if i == 0:
                continue
            else:
                if score_list[i] > score_list[winner]:
                    winner = i
                elif score_list[i] == score_list[winner]:
                    if turns_list[i] < turns_list[winner]:
                        winner = i
        print(f"Player {winner+1} is the winner.")
    else:
        print("You entered invalid no. of players.")


if __name__ == "__main__":
    main()
