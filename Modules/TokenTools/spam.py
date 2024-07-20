import requests, os, json, threading
from colorama import Fore

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_token():
    f = open("settings.json")
    data = json.load(f)
    token_ = data["token"]
    return token_

def token_spam():
    clear()
    def spam_(channel, message, ammount):
        for i in range(int(ammount)):
            url = f"https://discord.com/api/v9/channels/{channel}/messages"
            r = requests.post(url, json={'content': message}, headers={'Authorization':token})
            if r.status_code == 200:
                print(green + "[+] Sent Message")
            else:
                print(yellow + "[!] Rate Limited")

    print(cyan + "Make Sure Your Token Is In settings.json")
    channel = input(cyan + "Channel ID: ")
    message = input(cyan + "Message: ")
    ammount = input(cyan + "Time To Spam: ")
    token = get_token()

    clear()
    input(cyan + f"Message -> {message} | Channel ID -> {channel} | Press Enter To Start > \n")

    threads = []
    for i in range(20):
        t = threading.Thread(target=spam_, args=(channel, message, ammount))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
                
    ag = input(cyan + "\nStopped Spamming. | Do You Want To Spam Again? Y/n > ")
    if ag == "Y":
        clear()
        token_spam()
    else:
        clear()
        from main import main
        main()