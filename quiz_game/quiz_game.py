import sys


def main():
    quiz()


def quiz():
    res = input("do you wanna play quiz game! ").strip().lower()
    if res == "no" or res == "n":
        sys.exit("ok that's fine :)")
    if res == "yes" or res == "y":
        print("ok! lets get started")
        score = 0
        ans = input("what does cpu stand for? ").lower().strip()
        if ans == "central processing unit":
            print("correct")
            score += 1
        else:
            print("incorrect")
        ans = input("what's your capital of India!").lower().strip()
        if ans == "delhi":
            print("correct")
            score += 1
        else:
            print("incorrect")
        ans = input("what does ram stand for? ").lower().strip()
        if ans == "random access memory":
            print("correct")
            score += 1
        else:
            print("incorrect")
        ans = input("what does psu stand for? ").lower().strip()
        if ans == "power supply unit":
            print("correct")
            score += 1
        else:
            print("incorrect")
        ans = input("what does gpu stand for? ").lower().strip()
        if ans == "graphical processing unit":
            print("correct")
            score += 1
        else:
            print("incorrect")
        print(f"your scores are {score}")
    else:
        print("invalid response")


if __name__ == "__main__":
    main()
