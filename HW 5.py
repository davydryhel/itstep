import colorama
from colorama import Fore, init
init(autoreset=True)

def green(text):
    print(Fore.GREEN + text)

def red(text):
    print(Fore.RED + text)

green("OK")
red("ERROR")