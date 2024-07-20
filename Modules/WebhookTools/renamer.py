import requests, os
from colorama import Fore

cyan = Fore.CYAN
green = Fore.GREEN
red = Fore.RED

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def rename_webhook():
    clear()
    webhook_url = input(cyan + "Webhook: ")
    new_name = input(cyan + "Enter the new name: ")
    r = requests.patch(webhook_url, json={"name": new_name})
    if r.status_code == 200:
        print(green + f"[+] Webhook Renamed to {new_name} successfully")
    else:
        print(red + f"[!] Failed to rename webhook: {r.text}")
    input(cyan + "Press Enter to go back > ")

    from main import main
    clear()
    main()