import time, os
from colorama import Fore

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from Modules.TokenTools.raid import raid
from Modules.TokenTools.spam import token_spam
from Modules.TokenTools.hype import hype
from Modules.TokenTools.checker import checker
from Modules.TokenTools.status_rot import rotate
from Modules.TokenTools.reaction import reactor

from Modules.WebhookTools.spam import webhook_spam
from Modules.WebhookTools.delete import hook_del
from Modules.WebhookTools.renamer import rename_webhook

cyan = Fore.CYAN
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW

def main():
    def invalid():
        options = [1, 2, "1", "2", "x"]
        if op == "x":
            print(yellow + "\nClosing PYI...")
            time.sleep(1.5)
            exit()

        if op in options:
            pass
        else:
            print(red + "\n[!] Invalid Option")
            time.sleep(1.5)
            clear()
            main()

    print(cyan + r"""
     _______      _______ 
    |  __ \ \   / /_   _|
    | |__) \ \_/ /  | | Dev: ISellStuff  
    |  ___/ \   /   | | Exit -> [x] 
    | |      | |   _| |_ 
    |_|      |_|  |_____|                
        [ Main Menu ]
          
    [1] Token Tools
    [2] Webhook Tools                  """)
    op = input(cyan + "> ")
    invalid()

    if op == "1":
        def invalid_1():
            options = ["1", "2", "3", "4", "5", "6", "w", "x"]
            if opk == "x":
                print(yellow + "\nClosing PYI...")
                time.sleep(1.5)
                exit()
            elif opk == "w":
                clear()
                main()

            if opk in options:
                pass
            else:
                print(red + "\n[!] Invalid Option")
                time.sleep(1.5)
                clear()
                main()

        clear()
        print(cyan + r"""
     _______      _______ 
    |  __ \ \   / /_   _|
    | |__) \ \_/ /  | | Main Menu -> [w]
    |  ___/ \   /   | | Exit -> [x] 
    | |      | |   _| |_ 
    |_|      |_|  |_____|
        [ Token Tools]                  
     
    [1] Raid
    [2] Spam
    [3] HypeSquad Joiner
    [4] Token Checker
    [5] Status Rotator
    [6] Reaction Spam      """)
        opk = input(cyan + "> ")
        invalid_1()

        if opk == "1":
            raid()
        elif opk == "2":
            token_spam()
        elif opk == "3":
            hype()
        elif opk == "4":
            checker()
        elif opk == "5":
            clear()
            print(green + "Note: You Will Have To re open this again if you want to use other tools")
            print()
            rotate()
        elif opk == "6":
            reactor()

    elif op == "2":
        def invalid_2():
            options = [1,"1",2, "2",3, "3", "w","x"]
            if opw == "x":
                print(yellow + "\nClosing PYI...")
                time.sleep(1.5)
                exit()
            elif opw == "w":
                clear()
                main()

            if opw in options:
                pass
            else:
                print(red + "\n[!] Invalid Option")
                time.sleep(1.5)
                clear()
                main()

        clear()
        print(cyan + r"""
     _______      _______ 
    |  __ \ \   / /_   _|
    | |__) \ \_/ /  | | Main Menu -> [w]
    |  ___/ \   /   | | Exit -> [x] 
    | |      | |   _| |_ 
    |_|      |_|  |_____|
        [ Webhook Tools]                  
     
    [1] Webhook Spammer
    [2] Webhook Deleter
    [3] Webhook Renamer               """)
        opw = input(cyan + "> ")
        invalid_2()

        if opw == "1":
            webhook_spam()
        elif opw == "2":
            hook_del()
        elif opw == "3":
            rename_webhook()

main()