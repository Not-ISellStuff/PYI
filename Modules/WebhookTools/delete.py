import requests
import os
from colorama import Fore, init

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hook_del():
    clear()
    webhook_url = input(cyan + "Webhook: ")
    requests.post(webhook_url, json={"content": "Your Webhook Is Going To Be Deleted in 5 Seconds"})
    countdown = 5
    while countdown > 0:
        requests.post(webhook_url, json={"content": str(countdown)})
        countdown -= 1

    requests.post(webhook_url, json={"content": "Deleted hahaha retard"})
    response = requests.delete(webhook_url)

    if response.status_code == 204:
        print(green + "\n[+] Webhook deleted successfully")
    else:
        print(red + "\n[-] Failed to delete webhook")

    input(cyan + "Press Enter to go back > ")

    from main import main
    clear()
    main()