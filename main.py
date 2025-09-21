import requests
import time
import os
from datetime import datetime
from colorama import Fore, Style, init
from pystyle import Colors, Colorate, Center

r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
rs = Fore.RESET

os.system('title ^| Eternal IMP ^| Discord.gg/input ^| Token Checker ^|')
def ascii1():
    print(Colorate.Horizontal(Colors.blue_to_white,("""                     

                                    ______  _______     ________              __            
                                   /  _/  |/  / __ \   / ____/ /_  ___  _____/ /_____  _____
                                   / // /|_/ / /_/ /  / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
                                 _/ // /  / / ____/  / /___/ / / /  __/ /__/ ,< /  __/ /    
                                /___/_/  /_/_/       \____/_/ /_/\___/\___/_/|_|\___/_/     
                                                            
""")))

def get_time():
    return datetime.now().strftime('%H:%M:%S')

def mask_token(token):
    return token[:-9] + '*' * 9

def check_token(token):
    headers = {"Authorization": token}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
    masked_token = mask_token(token)
    if response.status_code == 200:
        print(f" {get_time()} {g}[{rs}+{g}]{rs} Valid token {g}>>{rs} {masked_token}")
        with open("input/valid.txt", "a") as valid_file:
            valid_file.write(token + "\n")
    else:
        print(f" {get_time()} {r}[{rs}-{r}]{rs} Invalid token {r}>>{rs} {masked_token}")

def main():
    os.system("cls" if os.name == "nt" else "clear")
    ascii1()
    print(f" {get_time()} {g}[{rs}+{g}]{rs} Checking tokens...")
    
    if not os.path.exists("input/tokens.txt"):
        print(f" {get_time()} {r}[{rs}-{r}]{rs} Error {r}>>{rs} input/tokens.txt not found!")
        return
    
    with open("input/tokens.txt", "r") as file:
        tokens = file.read().splitlines()
    
    for token in tokens:
        check_token(token)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
