from pw_encrypter import encrypt, decrypt
import csv


def main():
    manager()


def manager():
    while True:
        mode = input("Would you like to add a new password (A) or view the existing one (V), press (Q) to quit.").lower()
        if mode == "a":
            add()
        elif mode == "v":
            view()
        elif mode == "q":
            break
        else:
            print("invalid character.")


def add():
    master = input("Enter master password? ")
    master = master.encode()
    with open("mp.key", "rb") as file:
        key = file.read()
        mp = decrypt(key)
    if master == mp:
        name = input("Name: ")
        password = input("Password: ")
        with open("password_manager.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "password"])
            # writer.writeheader()
            writer.writerow({"name": name, "password": encrypt(password).decode()})
    else:
        print("Wrong Master Password")


def view():
    mp = input("Enter Master Password.")
    mp = mp.encode()
    with open("mp.key", "rb") as file:
        key = file.read()
        key = decrypt(key)
    if mp == key:
        with open("password_manager.csv", "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                ep = line['password']
                ep = ep.encode()
                print(f"Name: {line['name']}, Password: {decrypt(ep).decode()}")
    else:
        print("Wrong Master Password.")


if __name__ == "__main__":
    main()

