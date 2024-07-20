import requests, os
from colorama import Fore

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def reactor():

    clear()

    def r(token):
        re = requests.put(a, headers={"Authorization":token}, data=d)
        if re.status_code == 204:
            print(green + "[+] Reacted")
        elif re.status_code == 401:
            print(red + "[-] Invalid Token")
        elif re.status_code == 429:
            print(yellow + "[!] Rate Limited")
        else:
            print(yellow + "[-] Error")

    channel = input("Channel ID: ")
    message = input("Message ID: ")
    
    a = f"https://discord.com/api/v9/channels/{channel}/messages/{message}/reactions/%F0%9F%A5%B6/%40me?location=Message&type=0"
    d = "location=Message&type=0"
    input(cyan + "Press Enter To Continue > ")
    print()

    with open("tokens.txt", "r") as f:
        tokens = [line.strip() for line in f.readlines()]
    for i in tokens:
        tk = i.strip()
        r(tk) 

    input(cyan + "\nPress Enter to go back > ")
    from main import main
    clear()
    main()       