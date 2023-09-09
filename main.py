import sys
from cleanfolder import start


def adressbook():
    return "adressbook"


def notebook():
    return "notebook"


def cleanfolder():
    return start()


def exiting():
    print("Good bye!")
    sys.exit()


def main_menu():
    print(f"Hello, I'm your personal assistant. You can enter the number in the command line.\n1 - phone book.\n2 - notebook.\n3 - clean the folder, put it in order.\n4 - exit")
    
    comands = {
    "1": adressbook,
    "2": notebook,
    "3": cleanfolder,
    "4": exiting,
    }
    
    while True:
        user_input = input(">>> ")
        if user_input not in comands.keys():
            print("I don't understand such commands. Try entering 1, 2, 3 or 4.")
        else:
            for k, v in comands.items():
                if user_input == k:
                    print(v())
                else:
                    pass
                
            
if __name__ == "__main__":
    main_menu()