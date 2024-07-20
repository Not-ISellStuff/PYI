import requests, threading, os, sys
from colorama import Fore

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW


def raid():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    clear()
    def raid_(token, channel, message, ammount):
        for i in range(int(ammount)):
            url = f"https://discord.com/api/v9/channels/{channel}/messages"
            r = requests.post(url, json={'content': message}, headers={'Authorization': token})
            if r.status_code == 200:
                print(green + "[+] Sent Message")
            else:
                print(yellow + "[!] Rate Limited")
                
    channel = input(cyan + "Channel ID: ")
    message = input(cyan + "Message: ")
    ammount = input(cyan + "Ammount Of Messages To Send: ")
    clear()
    url = f"https://discord.com/api/v9/channels/{channel}/messages"
    print(cyan + f"Threads -> 20 | Message -> {message} | Press Enter > \n")

    threads = []
    with open("tokens.txt", "r") as f:
        tokens = [line.strip() for line in f.readlines()]

    for i in range(20):
        for token in tokens:
            t = threading.Thread(target=raid_, args=(token, channel, message, ammount))
            t.start()
            threads.append(t)
    for t in threads:
        t.join()
                
    ag = input(cyan + "\nFinished Raiding. | Do You Want To Raid Again? Y/n > ")
    if ag == "Y":
        clear()
        raid()
    else:
        clear()
        from main import main
        main()