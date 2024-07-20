import requests, time, random, json
from colorama import Fore

def get_token():
    f = open("settings.json")
    data = json.load(f)
    token_ = data["token"]
    return token_
def get_stat1():
    f = open("settings.json")
    data = json.load(f)
    fr = data["status_message_1"]
    return fr
def get_stat2():
    f = open("settings.json")
    data = json.load(f)
    tw = data["status_message_2"]
    return tw


def rotate():
    with open("Modules/Data/status.txt", "w") as f:
        pass

    tk = get_token()
    stat1 = get_stat1()
    stat2 = get_stat2()
    status_messages = [stat1, stat2]
    def set_status(status):
        headers = {
            "Authorization":tk,
            "Content-Type": "application/json"
        }
        data = {"custom_status": {"text": status}}
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=data)
        if r.status_code == 200:
            print(Fore.GREEN + "[+] Changed Status")
        else:
            print(Fore.YELLOW + "[!] RATE LIMIT")
    while True:
        status = random.choice(status_messages)
        set_status(status)
        time.sleep(1)
