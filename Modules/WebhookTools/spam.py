import requests, threading, os, time, random
from colorama import Fore

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW


def webhook_spam():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    clear()
    proxy_list = []
    prox = requests.get("https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&proxy_format=ipport&format=text&timeout=20000")
    for line in prox.text.splitlines():
         proxy_list.append({"http": f"http://{line}"})

    def spam_(hook, message, ammount):
        for i in range(int(ammount)):
            url = hook
            proxy = random.choice(proxy_list)
            r = requests.post(url, json={'content': message}, proxies=proxy, timeout=10)
            if r.status_code == 204:
                print(green + "[+] Sent Message")
            else:
                print(yellow + "[!] Rate Limited")
    
    hook = input(cyan + "Webhook: ")
    message = input(cyan + "Message: ")
    ammount = input(cyan + "Ammount Of Messages To Send: ")
    clear()
    print(cyan + f"Threads -> 20 | Message -> {message} | Press Enter > \n")

    threads = []
    for i in range(50):
        t = threading.Thread(target=spam_, args=(hook, message, ammount))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
                
    ag = input(cyan + "\nFinished Spamming. | Do You Want To Spam Webhook Again? Y/n > ")
    if ag == "Y":
        clear()
        webhook_spam()
    else:
        clear()
        from main import main
        main()