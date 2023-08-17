import sys
import clipboard
import json

""" data = clipboard.paste()
print(data) """

SAVED_DATA = "clipboard.json"

def save_items(filepath, data):
    with open(filepath, "w") as f: #w: write
        json.dump(data, f)

def load_items(filepath):
    try:
        with open(filepath, "r") as f: #r: read
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print("data has been saved!")

    elif command == "load":
        key = input("Enter a key: ")
        data = load_items(SAVED_DATA)
        if key in data:
            print("The value is", data[key])
            clipboard.copy(data[key])
            print("Alrealy copied!")
        else:
            print("The key was not found :(")

    elif command == "list":
        print(data)

    else:
        print("Unknow command")

else:
    print("Please pass exatly one command")




