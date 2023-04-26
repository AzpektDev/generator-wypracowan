# you have /history folder. it contains files named username-password-date-history.txt. select all user files after prompt
from colorama import Fore, Back, Style
from getpass import getpass
import glob

user = input(Fore.BLUE + "login: " + Style.RESET_ALL)
password = getpass(Fore.BLUE + "password: " + Style.RESET_ALL)

files = glob.glob(f"history/{user}-{password}-*-history.txt")

for index, file in enumerate(files):
    with open(file, "r") as f:
        content = f.read()
        topic = content.split("\n")[0].split(": ")[1]
        content = content.split("\n")[1]
        print(f"{index + 1}: {Fore.GREEN}{topic}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{content}{Style.RESET_ALL}")

