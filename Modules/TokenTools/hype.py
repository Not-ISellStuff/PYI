import requests, threading, os, random
from colorama import Fore

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hype():
    clear()
    input(cyan + "Press Enter To Start > ")
    api = 'https://discord.com/api/v9/hypesquad/online'
    print()

    def join(token):
        houses = [1,2,3,4]
        house = random.choice(houses)

        h = {"Authorization":token}
        j = {'house_id':house}
        r = requests.post(api, headers=h, json=j)
        if r.status_code == 204:
            print(green + "[+] Joined HypeSquad")
        elif r.status_code == 429:
            print(yellow + "[!] Rate Limited")
        elif r.status_code == 401:
            print(red + "[-] Invalid Token")
        else:
            print(green + "[-] Invalid Token")

    threads = []
    with open("tokens.txt", "r") as f:
        tokens = [line.strip() for line in f.readlines()]
    for token in tokens:
        t = threading.Thread(target=join, args=(token,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    input(cyan + "\nPress Enter to go back > ")
    from main import main
    clear()
    main()