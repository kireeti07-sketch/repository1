from datetime import datetime

def diary_entry():
    today = datetime.now()
    name = today.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"

    print("1. Create new file")
    print("2. Append to file")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        file = open(name, "w")
    elif choice == "2":
        file = open(name, "a")
    else:
        return

    entry = input("Write your diary entry: ")
    file.write(f"[{today}] {entry}\n")  # Using f-string for formatting
    file.close()

    print("Saved in " + name)

diary_entry()
