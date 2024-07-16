import sys
from typing import List
from pathlib import Path
from colorama import Fore


def get_structure(entry: List[str]) -> str:
    if len(entry) < 2:
        print("Please, enter path to the folder")
        return ""

    path = Path(entry[1])
    if not Path.exists(path):
        print("Please, enter correct path")
        return ""

    result = f"{Fore.LIGHTYELLOW_EX}{path.name}/{Fore.RESET}\n"
    for item in path.glob('*'):
        if item.is_dir():
            result += f"{" " * 4}{Fore.LIGHTYELLOW_EX}{item.name}/{Fore.RESET}\n"
        if item.is_file():
            result += f"{" " * 4}{Fore.LIGHTMAGENTA_EX}{item.name}{Fore.RESET}\n"

    return result


print(get_structure(sys.argv))
