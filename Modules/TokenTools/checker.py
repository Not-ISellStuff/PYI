import requests, threading, os, queue
from colorama import Fore

cyan = Fore.CYAN
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def checker():
    with open("valid_tokens.txt", "w") as f:
        pass

    clear()
    threads_ = input(cyan + "Threads: ")
    print()

    def check(token):
        h = {"Authorization":token}
        u = "https://discord.com/api/v9/quests/@me"
        r = requests.get(u, headers=h)
        if r.status_code == 200:
            print(green + "[+] Valid Token")
            with open("valid_tokens.txt", "a") as f:
                f.write(f"{token}\n")
        elif r.status_code == 401:
            print(red + "[-] Invalid Token")
        elif r.status_code == 429:
            print(yellow + "[!] Rate Limited")
        else:
            print(red +"[-] Invalid Token")

    def worker(q):
        while not q.empty():
            token = q.get()
            check(token)
            q.task_done()
    q = queue.Queue()
    with open("tokens.txt", "r") as f:
        tokens = [line.strip() for line in f.readlines()]
    for token in tokens:
        q.put(token)
    threads = []
    for i in range(int(threads_)):
        t = threading.Thread(target=worker, args=(q,))
        t.start()
        threads.append(t)

    q.join()
    for t in threads:
        t.join()